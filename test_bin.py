import sys
from pathlib import Path

try:
    import phreeqc
except ImportError as e:
    sys.path.append(str(Path.cwd() / "src"))
    import phreeqc
