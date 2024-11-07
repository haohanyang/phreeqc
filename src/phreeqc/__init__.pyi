from typing import List

class Phreeqc:
    def __init__(self) -> None:
        """
        Create a Phreeqc instance.
        """
        ...

    def load_database(self, path: str) -> None:
        """
        Load the specified database file into phreeqc.

        :param path: The path of the phreeqc database to load. The full path (or relative path \
            with respect to the working directory) will be required if the file is not in the current working directory
        """
        ...

    def run_file(self, path: str) -> None:
        """
        Runs the specified phreeqc input file.

        :param path: The path of the phreeqc input file to run.
        """
        ...

    def run_string(self, input: str) -> None:
        """
        Runs the specified string as input to phreeqc.

        :param input: String containing phreeqc input.
        """
        ...

    def get_selected_output(self) -> List[List]:
        """
        Get the selected output.

        :return: A 2d-array consisting of each row from the selected output
        """
        ...
