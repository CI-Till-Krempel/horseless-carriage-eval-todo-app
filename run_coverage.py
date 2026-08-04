import subprocess
import sys

def run_cov():
    cmd = [sys.executable, "-m", "pytest", "--cov=app", "--cov-report=term-missing"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(res.stdout)
    print(res.stderr)
    sys.exit(res.returncode)

if __name__ == "__main__":
    run_cov()
