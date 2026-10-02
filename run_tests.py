import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
sys.exit(subprocess.call([sys.executable, "-m", "pytest"]))
