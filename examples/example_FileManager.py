import subprocess
from utlib import FileManager

subprocess.run(["source", "venv/bin/activate"])


fm = FileManager("examples/demo.txt")
fm.delete()
