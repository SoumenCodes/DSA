import subprocess
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = f"update_{timestamp}.txt"

# Log the working directory
subprocess.run(['git', 'status'], shell=True)  # Debug: Ensure you're in the repo

with open(filename, 'w') as f:
    f.write(f"Auto-commit at {timestamp}")

try:
    subprocess.run(['git', 'add', filename], check=True, shell=True)
    subprocess.run(['git', 'commit', '-m', f'Add {filename}'], check=True, shell=True)
    subprocess.run(['git', 'push', 'origin', 'main'], check=True, shell=True)  # Change 'main' if needed
    print(f"Pushed {filename} to GitHub!")
except Exception as e:
    print(f"Error: {e}")
    with open("error_log.txt", 'a') as log:
        log.write(f"{timestamp} - {e}\n")