from typing import Union, TypeAlias, Literal

BUILT_IN_DB_FILE: TypeAlias = Literal[
    "Amm.dat",
    "core10.dat",
    "llnl.dat",
    "phreeqc.dat",
    "Tipping_Hurley.dat",
    "frezchem.dat",
    "phreeqc_rates.dat",
    "wateq4f.dat",
    "ColdChem.dat",
    "iso.dat",
    "PHREEQC_ThermoddemV1.10_15Dec2020.dat",
    "Concrete_PHR.dat",
    "Kinec.v2.dat",
    "minteq.dat",
    "pitzer.dat",
    "Concrete_PZ.dat",
    "Kinec_v3.dat",
    "minteq.v4.dat",
    "sit.dat",
]

class Phreeqc:
    def __init__(self) -> None: ...

    # ── Accumulate ────────────────────────────────────────────────────────────

    def AccumulateLine(self, line: str) -> None:
        """Accumulate line(s) for input to phreeqc.

        :param line: The line(s) to add.
        :raises MemoryError: If out of memory.
        """
        ...

    def ClearAccumulatedLines(self) -> None:
        """Clear the accumulated input buffer."""
        ...

    def GetAccumulatedLines(self) -> str:
        """Retrieve the accumulated input string.

        :returns: The accumulated input string.
        """
        ...

    def OutputAccumulatedLines(self) -> None:
        """Output the accumulated input buffer to stdout."""
        ...

    def RunAccumulated(self) -> int:
        """Run the input buffer accumulated via AccumulateLine.

        :returns: Number of errors encountered.
        """
        ...
    # ── Errors ────────────────────────────────────────────────────────────────

    def AddError(self, error_msg: str) -> int:
        """Append an error message and increment the error count.

        :param error_msg: The error message to display.
        :returns: The current error count.
        """
        ...

    def GetErrorFileName(self) -> str: ...
    def GetErrorFileOn(self) -> bool: ...
    def GetErrorOn(self) -> bool: ...
    def GetErrorString(self) -> str:
        """Retrieve error messages from the last run.

        :returns: A string containing error messages.
        """
        ...

    def GetErrorStringLine(self, n: int) -> str:
        """Retrieve the given error line.

        :param n: Zero-based line index.
        :returns: The line, or empty string if out of range.
        """
        ...

    def GetErrorStringLineCount(self) -> int: ...
    def GetErrorStringOn(self) -> bool: ...
    def OutputErrorString(self) -> None: ...
    def SetErrorFileName(self, filename: str) -> None: ...
    def SetErrorFileOn(self, value: bool) -> None: ...
    def SetErrorOn(self, value: bool) -> None: ...
    def SetErrorStringOn(self, value: bool) -> None: ...

    # ── Warnings ──────────────────────────────────────────────────────────────

    def AddWarning(self, warning_msg: str) -> int:
        """Append a warning message and increment the warning count.

        :param warning_msg: The warning message to display.
        :returns: The current warning count.
        """
        ...

    def GetWarningString(self) -> str: ...
    def GetWarningStringLine(self, n: int) -> str: ...
    def GetWarningStringLineCount(self) -> int: ...
    def OutputWarningString(self) -> None: ...

    # ── Components ────────────────────────────────────────────────────────────

    def GetComponent(self, n: int) -> str:
        """Retrieve a component by zero-based index.

        :param n: Zero-based component index.
        :returns: Component name, or empty string if out of range.
        """
        ...

    def GetComponentCount(self) -> int:
        """Retrieve the number of components.

        :returns: The current count of components.
        """
        ...

    def GetComponents(self) -> list[str]:
        """Return all components as a list of strings.

        :returns: A list of component name strings.
        """
        ...

    def ListComponents(self) -> list[str]:
        """Retrieve the current list of components.

        :returns: A list of component name strings.
        """
        ...
    # ── Database ──────────────────────────────────────────────────────────────

    def LoadDatabase(self, filename: str) -> int:
        """Load the specified database file into phreeqc.

        All previous definitions are cleared.
        :param filename: Path to the phreeqc database file.
        :returns: Number of errors encountered.
        """
        ...

    def LoadDatabaseString(self, input: str) -> int:
        """Load the specified string as a database into phreeqc.

        All previous definitions are cleared.
        :param input: String containing phreeqc database data.
        :returns: Number of errors encountered.
        """
        ...

    def LoadBuiltInDatabase(self, name: BUILT_IN_DB_FILE) -> int:
        """Load one of the built-in PHREEQC database files bundled with this package.

        All previous definitions are cleared.
        :param name: Filename of the built-in database (e.g. ``"phreeqc.dat"``).
        :returns: Number of errors encountered.
        :raises FileNotFoundError: If *name* is not found in the bundled databases.
        """
        ...

    @staticmethod
    def ListBuiltInDatabases() -> list[str]:
        """Return the names of all built-in database files bundled with this package.

        :returns: Sorted list of database filenames (e.g. ``["Amm.dat", ...]``).
        """
        ...
    # ── Run ───────────────────────────────────────────────────────────────────

    def RunFile(self, filename: str) -> int:
        """Run the specified phreeqc input file.

        :param filename: Path to the phreeqc input file.
        :returns: Number of errors encountered.
        """
        ...

    def RunString(self, input: str) -> int:
        """Run the specified string as phreeqc input.

        :param input: String containing phreeqc input.
        :returns: Number of errors encountered.
        """
        ...
    # ── Selected Output ───────────────────────────────────────────────────────

    def GetCurrentSelectedOutputUserNumber(self) -> int:
        """Retrieve the current SELECTED_OUTPUT user number (default 1).

        :returns: The current user number.
        """
        ...

    def GetNthSelectedOutputUserNumber(self, n: int) -> int:
        """Retrieve the nth defined SELECTED_OUTPUT user number.

        :param n: Zero-based index.
        :returns: The user number; negative on error.
        """
        ...

    def GetSelectedOutputColumnCount(self) -> int:
        """Retrieve the number of columns in the selected-output buffer.

        :returns: The number of columns.
        """
        ...

    def GetSelectedOutputCount(self) -> int:
        """Retrieve the count of SELECTED_OUTPUT blocks defined.

        :returns: Number of SELECTED_OUTPUT blocks.
        """
        ...

    def GetSelectedOutputFileName(self) -> str: ...
    def GetSelectedOutputFileOn(self) -> bool: ...
    def GetSelectedOutputRowCount(self) -> int:
        """Retrieve the number of rows in the selected-output buffer.

        Row 0 is the header row; data rows start at index 1.
        :returns: The number of rows (including header).
        """
        ...

    def GetSelectedOutputString(self) -> str: ...
    def GetSelectedOutputStringLine(self, n: int) -> str: ...
    def GetSelectedOutputStringLineCount(self) -> int: ...
    def GetSelectedOutputStringOn(self) -> bool: ...
    def GetSelectedOutputValue(self, row: int, col: int) -> Union[int, float, str]:
        """Return the value at the specified row and column.

        Row 0 contains column headings; data starts at row 1.
        :param row: The row index.
        :param col: The column index.
        :returns: int, float, or str depending on the cell type.
        :raises IndexError: If row or column is out of range.
        :raises ValueError: If the argument or VAR type is invalid.
        :raises MemoryError: If memory allocation fails.
        """
        ...

    def GetSelectedOutput(self) -> dict[str, list[Union[int, float, str]]]:
        """Return SELECTED_OUTPUT as a column-oriented dictionary.

        :returns: Dict mapping column names to lists of values,
                  e.g. ``{"pH": [7.0, 6.8], "Ca(mol/kgw)": [1e-3, 2e-3]}``.
        """
        ...

    def SetCurrentSelectedOutputUserNumber(self, n: int) -> None:
        """Set the current SELECTED_OUTPUT user number.

        :param n: User number as specified in the SELECTED_OUTPUT block.
        :raises ValueError: If the user number has not been defined.
        """
        ...

    def SetSelectedOutputFileName(self, filename: str) -> None: ...
    def SetSelectedOutputFileOn(self, value: bool) -> None: ...
    def SetSelectedOutputStringOn(self, value: bool) -> None: ...

    # ── Dump ──────────────────────────────────────────────────────────────────

    def GetDumpFileName(self) -> str: ...
    def GetDumpFileOn(self) -> bool: ...
    def GetDumpString(self) -> str: ...
    def GetDumpStringLine(self, n: int) -> str: ...
    def GetDumpStringLineCount(self) -> int: ...
    def GetDumpStringOn(self) -> bool: ...
    def SetDumpFileName(self, filename: str) -> None: ...
    def SetDumpFileOn(self, value: bool) -> None: ...
    def SetDumpStringOn(self, value: bool) -> None: ...

    # ── Log ───────────────────────────────────────────────────────────────────

    def GetLogFileName(self) -> str: ...
    def GetLogFileOn(self) -> bool: ...
    def GetLogString(self) -> str: ...
    def GetLogStringLine(self, n: int) -> str: ...
    def GetLogStringLineCount(self) -> int: ...
    def GetLogStringOn(self) -> bool: ...
    def SetLogFileName(self, filename: str) -> None: ...
    def SetLogFileOn(self, value: bool) -> None: ...
    def SetLogStringOn(self, value: bool) -> None: ...

    # ── Output ────────────────────────────────────────────────────────────────

    def GetOutputFileName(self) -> str: ...
    def GetOutputFileOn(self) -> bool: ...
    def GetOutputString(self) -> str: ...
    def GetOutputStringLine(self, n: int) -> str: ...
    def GetOutputStringLineCount(self) -> int: ...
    def GetOutputStringOn(self) -> bool: ...
    def SetOutputFileName(self, filename: str) -> None: ...
    def SetOutputFileOn(self, value: bool) -> None: ...
    def SetOutputStringOn(self, value: bool) -> None: ...

    # ── Instance / Version ────────────────────────────────────────────────────

    def GetId(self) -> int:
        """Retrieve the unique id of this instance (incremented from 0).

        :returns: The id.
        """
        ...

    @staticmethod
    def GetVersionString() -> str:
        """Retrieve the IPhreeqc version string (e.g. '3.7.3-15968').

        :returns: The version string.
        """
        ...
