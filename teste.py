import os
import subprocess

list_files = subprocess.run(["ls", "-l"])
print(list_files)
