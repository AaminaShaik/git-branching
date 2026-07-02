import subprocess
import OS linux add windows

process = subprocess.Popen(
    ["python", "hello.py"]
)
port = 3000
print(f"Python script started with PID: {process.pid}")
