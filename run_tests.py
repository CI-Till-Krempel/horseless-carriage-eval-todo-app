import subprocess
result = subprocess.run(['pytest', '-v'], capture_output=True, text=True)
print("STDOUT:\n", result.stdout)
print("STDERR:\n", result.stderr)
print("RETCODE:", result.returncode)
