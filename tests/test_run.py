import subprocess
import pytest

def test_run_pytest():
    result = subprocess.run(['pytest'], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    assert result.returncode == 0, f"Pytest failed:\n{result.stdout}\n{result.stderr}"
