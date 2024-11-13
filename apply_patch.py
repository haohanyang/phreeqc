import os.path
import subprocess

patch_path = os.path.abspath("cmake.patch")

subprocess.run(["git", "apply", patch_path], cwd="iphreeqc")
