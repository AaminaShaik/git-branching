import subprocess
import OS linux 

process = subprocess.Popen(
    ["python", "hello.py"]
)
port = 9000
print(f"Python script started with PID: {process.pid}")
