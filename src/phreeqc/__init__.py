from __future__ import annotations
from ._iphreeqc import _Phreeqc


class Phreeqc(_Phreeqc):
    def get_selected_output_value(self, row, col):
        res = super()._get_selected_output_value(row, col)
        return res[res[0] + 1]

    def get_selected_output(self):
        col_count = super().get_selected_output_column_count()
        row_count = super().get_selected_output_row_count()

        selected_output = {}

        for i in range(col_count):
            for j in range(row_count):
                if j == 0:
                    col_name = self.get_selected_output_value(j, i)
                    selected_output[col_name] = []
                else:
                    selected_output[col_name].append(
                        self.get_selected_output_value(j, i)
                    )
        return selected_output


__all__ = ["__doc__", "Phreeqc", "__version__"]
