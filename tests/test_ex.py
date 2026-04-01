import os.path
from phreeqc import Phreeqc

assert os.path.exists("tests/phreeqc.dat")


def test_ex2():
    # https://water.usgs.gov/water-resources/software/PHREEQC/documentation/phreeqc3-html/phreeqc3-64.htm#50593807_28577
    p = Phreeqc()
    p.load_database("tests/phreeqc.dat")
    p.run_string(
        """
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
USER_GRAPH 1 Example 2
        -headings Temperature Gypsum Anhydrite
        -chart_title "Gypsum-Anhydrite Stability"
        -axis_scale x_axis 25 75 5 0
        -axis_scale y_axis auto 0.05 0.1
        -axis_titles "Temperature, in degrees celsius" "Saturation index"
        -initial_solutions false
  -start
  10 graph_x TC
  20 graph_y SI("Gypsum") SI("Anhydrite")
  -end
END
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
USER_GRAPH 1 Example 2
        -headings Temperature Gypsum Anhydrite
        -chart_title "Gypsum-Anhydrite Stability"
        -axis_scale x_axis 25 75 5 0
        -axis_scale y_axis auto 0.05 0.1
        -axis_titles "Temperature, in degrees celsius" "Saturation index"
        -initial_solutions false
  -start
  10 graph_x TC
  20 graph_y SI("Gypsum") SI("Anhydrite")
  -end
END          
"""
    )

    selected_output = p.get_selected_output()
    assert len(selected_output["si_anhydrite"]) == 104
