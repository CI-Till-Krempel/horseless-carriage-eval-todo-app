#!/usr/bin/env python
import subprocess
import sys

def main():
    # Install requirements first to ensure environment has dependencies
    print("Installing requirements...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Run pytest with coverage
    print("Running pytest with coverage...")
    cmd = [sys.executable, "-m", "pytest", "--cov=app", "--cov-report=term-missing"]
    result = subprocess.run(cmd)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
