# PHREEQC

Python bindings of [IPHREEQC](https://www.usgs.gov/software/phreeqc-version-3)

## Install
```
pip install phreeqc
```
## Use
```py
from phreeqc import Phreeqc

p = Phreeqc()
error_count = p.load_database("phreeqc.dat")

if error_count != 0:
    raise RuntimeError("Failed to load database")

error_count = p.run_string(
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

if error_count != 0:
    raise RuntimeError("Failed to run string")

selected_output = p.get_selected_output()

print(selected_output)

```
## License
This project provides Python bindings for the iphreeqc software. The bindings are distributed under the [MIT License](/LICENSE), which applies to the Python and C++ binding code in this repository.

However, please note:

IPHREEQC, the underlying software to which these bindings provide access, is made available by the U.S. Geological Survey (USGS) under the terms described in its [User Rights Notice](/NOTICE). You can also find the full text of the license in the iphreeqc source or documentation.
By using this project, you agree to comply with the terms outlined in the iphreeqc license as well as the MIT license for the Python bindings.
