# Test if the output binary can be loaded by Python

import sys
import os
from pathlib import Path

if os.name == "nt":
    lib_path = Path.cwd() / "build" / "Release"
    if not lib_path.exists():
        lib_path = Path.cwd() / "build" / "Debug"
else:
    lib_path = Path.cwd() / "build"

sys.path.append(str(lib_path))

import phreeqc

print("phreeqc version", phreeqc.__version__)
