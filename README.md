# PHREEQC

Python bindings of [PHREEQC Version 3](https://www.usgs.gov/software/phreeqc-version-3)

The original C/C++ source code was downloaded from [IPhreeqc Modules](https://water.usgs.gov/water-resources/software/PHREEQC/iphreeqc-3.7.3-15968.tar.gz) made by USGS.

## Install
```
pip install phreeqc
```
## Use
```py
from phreeqc import Phreeqc


p = Phreeqc()
p.load_database("phreeqc.dat")
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
"""
)

selected_output = p.get_selected_output()
print(selected_output)
```
