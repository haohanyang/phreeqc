import tempfile

import pandas as pd
import streamlit as st

from phreeqc import Phreeqc

BUILTIN_DATABASES = Phreeqc.ListBuiltInDatabases()

st.set_page_config(page_title="PHREEQC Playground", layout="wide")
st.title("PHREEQC Playground")

# --- Sidebar: database selection ---
st.sidebar.header("Database")
db_source = st.sidebar.radio("Source", ["Built-in", "Upload"])

builtin_db: str | None = None
uploaded_db_path: str | None = None

if db_source == "Built-in":
    default_idx = (
        BUILTIN_DATABASES.index("phreeqc.dat")
        if "phreeqc.dat" in BUILTIN_DATABASES
        else 0
    )
    builtin_db = st.sidebar.selectbox("Database", BUILTIN_DATABASES, index=default_idx)
else:
    uploaded = st.sidebar.file_uploader("Upload .dat file", type=["dat"])
    if uploaded is not None:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".dat")
        tmp.write(uploaded.read())
        tmp.flush()
        uploaded_db_path = tmp.name

# --- Main: input ---
default_input = """\
TITLE Example 2.--Temperature dependence of solubility
                  of gypsum and anhydrite
SOLUTION 1 Pure water
        pH      7.0
        temp    25.0
EQUILIBRIUM_PHASES 1
        Gypsum          0.0     1.0
        Anhydrite       0.0     1.0
REACTION_TEMPERATURE 1
        25.0 75.0 in 51 steps
SELECTED_OUTPUT
        -file   ex2.sel
        -temperature
        -si     anhydrite  gypsum
END"""

input_text = st.text_area("PHREEQC input", value=default_input, height=300)

btn_col1, btn_col2 = st.columns([1, 1], gap="small")
with btn_col1:
    run = st.button("Run", type="primary", use_container_width=True)
with btn_col2:
    visualize = st.button(
        "Visualize...",
        disabled="last_df" not in st.session_state,
        use_container_width=True,
    )


@st.dialog("Visualize Output")
def show_chart_dialog(df: pd.DataFrame) -> None:
    numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    if len(numeric_cols) < 2:
        st.warning("Need at least two numeric columns to draw a chart.")
        return

    col1, col2 = st.columns(2)
    with col1:
        x_col = st.selectbox("X axis", numeric_cols, index=0)
    with col2:
        y_options = [c for c in numeric_cols if c != x_col]
        y_col = st.selectbox("Y axis", y_options, index=0)

    chart_type = st.radio("Chart type", ["Line", "Scatter"], horizontal=True)

    plot_df = df[[x_col, y_col]].set_index(x_col)
    if chart_type == "Line":
        st.line_chart(plot_df)
    else:
        st.scatter_chart(plot_df)


if run:
    if db_source == "Upload" and uploaded_db_path is None:
        st.error("Please upload a database file.")
    elif not input_text.strip():
        st.error("Input is empty.")
    else:
        try:
            pqc = Phreeqc()

            if db_source == "Built-in":
                db_errors = pqc.LoadBuiltInDatabase(builtin_db)
            else:
                db_errors = pqc.LoadDatabase(uploaded_db_path)

            if db_errors:
                st.error(
                    f"Database load failed ({db_errors} error(s)):\n\n{pqc.GetErrorString()}"
                )
                st.stop()

            run_errors = pqc.RunString(input_text)

            warnings = pqc.GetWarningString()
            if warnings.strip():
                st.warning(f"PHREEQC warnings:\n\n{warnings}")

            if run_errors:
                st.error(
                    f"Run failed ({run_errors} error(s)):\n\n{pqc.GetErrorString()}"
                )
                st.stop()

            output = pqc.GetSelectedOutput()
            if not output:
                st.warning(
                    "No SELECTED_OUTPUT data returned. "
                    "Make sure your input includes a SELECTED_OUTPUT block."
                )
            else:
                df = pd.DataFrame(output)
                st.session_state["last_df"] = df
                st.subheader("Selected Output")
                st.dataframe(df, width="stretch")
        except Exception as e:
            st.error(f"Unexpected error: {e}")

if visualize and "last_df" in st.session_state:
    show_chart_dialog(st.session_state["last_df"])
