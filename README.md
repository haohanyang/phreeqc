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
p.run_file("myfile.in")

print(p.get_selected_output())
```
