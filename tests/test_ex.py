import urllib.request
import re
import os
import os
from phreeqc import Phreeqc
from pytest import approx


def test_ex2():
    p = Phreeqc()

    with urllib.request.urlopen(
        "https://github.com/usgs-coupled/phreeqc3/raw/refs/heads/master/examples/ex2"
    ) as response:
        input_string = response.read().decode("utf-8")
        root = os.getenv("GITHUB_WORKSPACE")
        if root:
            database_path = os.path.join(root, "tests", "phreeqc.dat")
        else:
            database_path = os.path.join("tests", "phreeqc.dat")
        p.load_database(database_path)
        p.run_string(input_string)

    output = p.get_selected_output()

    expected = []
    with urllib.request.urlopen(
        "https://github.com/usgs-coupled/phreeqc3/raw/refs/heads/master/examples/ex2.sel"
    ) as response:
        for line in response.read().decode("utf-8").split("\n"):
            line = line.strip()
            if line:
                elems = line.split()
                for i in range(len(elems)):
                    if re.match(r"^-?\d+(?:\.\d+)$", elems[i]):
                        elems[i] = float(elems[i])
                    elif elems[i].isdigit():
                        elems[i] = int(elems[i])
                expected.append(elems)

    for i in range(len(expected)):
        for j in range(len(expected[0])):
            print(expected[i][j], output[i][j])
    if isinstance(expected[i][j], float):
        assert output[i][j] == approx(expected[i][j], abs=1e-4)
    else:
        assert output[i][j] == expected[i][j]
