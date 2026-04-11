import importlib.resources

from ._phreeqc import _Phreeqc as PhreeqcBase


class Phreeqc(PhreeqcBase):
    def GetSelectedOutput(self):
        col_count = self.GetSelectedOutputColumnCount()
        row_count = self.GetSelectedOutputRowCount()
        result = {}
        for col in range(col_count):
            col_name = str(self.GetSelectedOutputValue(0, col))
            result[col_name] = [
                self.GetSelectedOutputValue(row, col) for row in range(1, row_count)
            ]
        return result

    def GetComponents(self):
        return [self.GetComponent(i) for i in range(self.GetComponentCount())]

    def LoadBuiltInDatabase(self, name):
        db_ref = importlib.resources.files("phreeqc") / "databases" / name
        with importlib.resources.as_file(db_ref) as path:
            if not path.exists():
                msg = f"Built-in database {name!r} not found. "
                msg += "Use Phreeqc.ListBuiltInDatabases() to see available names."
                raise FileNotFoundError(msg)
            return self.LoadDatabase(str(path))

    @staticmethod
    def ListBuiltInDatabases():
        db_dir = importlib.resources.files("phreeqc") / "databases"
        with importlib.resources.as_file(db_dir) as path:
            return sorted(p.name for p in path.iterdir() if p.suffix == ".dat")


__all__ = ["__doc__", "Phreeqc", "__version__"]
