from __future__ import annotations
from ._iphreeqc import _Phreeqc


class Phreeqc(_Phreeqc):
    def get_selected_output(self):
        col_count = super().get_selected_output_column_count()
        row_count = super().get_selected_output_row_count()

        selected_output = {}

        for i in range(col_count):
            for j in range(row_count):
                print((i, j))
                if j == 0:
                    col_name = super().get_selected_output_value(j, i)
                    selected_output[col_name] = []
                else:
                    selected_output[col_name].append(
                        super().get_selected_output_value(j, i)
                    )
        return selected_output


__all__ = ["__doc__", "Phreeqc", "__version__"]
