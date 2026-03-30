import sys
from pathlib import Path

lib_path = Path.cwd() / "build" / "Release"

if lib_path.exists():
    sys.path.append(str(lib_path))
else:
    lib_path = Path.cwd() / "build" / "Debug"
    if lib_path.exists():
        sys.path.append(str(lib_path))
    else:
        raise Exception("phreeqc lib not found")

import phreeqc

print("phreeqc version", phreeqc.__version__)
