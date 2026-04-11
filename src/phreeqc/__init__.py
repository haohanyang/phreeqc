from __future__ import annotations
from typing import TypeAlias, Literal
import importlib.resources
from typing import Union

from ._phreeqc import _Phreeqc as PhreeqcBase

built_in_db_files = [
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


class Phreeqc(PhreeqcBase):
    """Python interface to IPhreeqc -- PHREEQC Version 3.

    Provides an interface to PHREEQC: A Computer Program for Speciation,
    Batch-Reaction, One-Dimensional Transport, and Inverse Geochemical Calculations.

    Example::

        phreeqc = Phreeqc()
        phreeqc.LoadDatabase("phreeqc.dat")
        phreeqc.RunString('''
            SOLUTION 1
                pH 7.0
                temp 25.0
            SELECTED_OUTPUT
                -reset false
                -pH
            END
        ''')
        data = phreeqc.GetSelectedOutput()
        # data == {"pH": [7.0]}
    """

    def GetSelectedOutput(self) -> dict[str, list[Union[int, float, str]]]:
        """Return the current SELECTED_OUTPUT data as a column-oriented dictionary.

        Row 0 of the selected output contains column headings; subsequent rows
        contain the numeric or string data. This method reads all rows and
        organises the values by column name.

        :returns: A dict mapping column names to lists of values, e.g.
                  ``{"pH": [7.0, 6.8], "Ca(mol/kgw)": [1e-3, 2e-3]}``.
        :see: SetCurrentSelectedOutputUserNumber, GetSelectedOutputColumnCount,
              GetSelectedOutputRowCount
        """
        col_count = self.GetSelectedOutputColumnCount()
        row_count = self.GetSelectedOutputRowCount()
        result: dict[str, list] = {}
        for col in range(col_count):
            col_name = str(self.GetSelectedOutputValue(0, col))
            result[col_name] = [
                self.GetSelectedOutputValue(row, col) for row in range(1, row_count)
            ]
        return result

    def GetComponents(self) -> list[str]:
        """Return all components as a list of strings.

        Convenience wrapper around GetComponent / GetComponentCount.

        :returns: A list of component name strings.
        :see: GetComponent, GetComponentCount, ListComponents
        """
        return [self.GetComponent(i) for i in range(self.GetComponentCount())]

    def LoadBuiltInDatabase(self, name: str) -> int:
        """Load a built-in PHREEQC database files bundled with this package.

        :param name: Filename of the built-in database (e.g. ``"phreeqc.dat"``).
        :returns: Number of errors encountered.
        :raises FileNotFoundError: If *name* is not found in the bundled databases.
        """
        db_ref = importlib.resources.files("phreeqc") / "databases" / name
        with importlib.resources.as_file(db_ref) as path:
            if not path.exists():
                msg = f"Built-in database {name!r} not found. "
                msg += "Use Phreeqc.ListBuiltInDatabases() to see available names."
                raise FileNotFoundError(msg)
            return self.LoadDatabase(str(path))

    @staticmethod
    def ListBuiltInDatabases() -> list[str]:
        """Return the names of all built-in database files bundled with this package.

        :returns: Sorted list of database filenames (e.g. ``["Amm.dat", ...]``).
        """
        db_dir = importlib.resources.files("phreeqc") / "databases"
        with importlib.resources.as_file(db_dir) as path:
            return sorted(p.name for p in path.iterdir() if p.suffix == ".dat")


__all__ = ["__doc__", "Phreeqc", "__version__"]
