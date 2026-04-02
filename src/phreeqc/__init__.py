from __future__ import annotations
from typing import Union

from ._phreeqc import _Phreeqc


class Phreeqc(_Phreeqc):
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


__all__ = ["__doc__", "Phreeqc", "__version__"]
