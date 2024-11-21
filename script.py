import re
import sys


def replace_version(filepath, new_version):
    """Replaces the version number in a file.

    Args:
        filepath: The path to the file.
        new_version: The new version string.
    """
    with open(filepath, "r") as f:
        content = f.read()

    # Use a regular expression to find and replace the version string
    new_content = re.sub(
        r'version\s*=\s*"(.*?)"', f'version = "{new_version}"', content
    )

    with open(filepath, "w") as f:
        f.write(new_content)


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "version":
        file_path = "pyproject.toml"
        new_version_number = sys.argv[2]
        replace_version(file_path, new_version_number)
    else:
        raise ValueError("Invalid input")
