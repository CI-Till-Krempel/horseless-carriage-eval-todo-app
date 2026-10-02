import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "Flask", "Flask-SQLAlchemy", "SQLAlchemy", "pytest"])
sys.exit(subprocess.call([sys.executable, "-m", "pytest"]))
