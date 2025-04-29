import subprocess
from datetime import datetime

# FIX: Replace colons with hyphens in filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Now: "2025-04-19_18-32-00"
filename = f"update_{timestamp}.txt"

try:
    # Debug: Print the working directory and Git status
    subprocess.run(['git', 'status'], shell=True)
    
    # Create a new file
    with open(filename, 'w') as f:
        f.write(f"Auto-commit at {timestamp}\n")
    
    # Git commands
    subprocess.run(['git', 'add', filename], check=True, shell=True)
    subprocess.run(['git', 'commit', '-m', f'Add {filename}'], check=True, shell=True)
    subprocess.run(['git', 'push', 'origin', 'main'], check=True, shell=True)
    print(f"Successfully pushed {filename} to GitHub!")
except Exception as e:
    print(f"Error: {e}")
    with open("error_log.txt", 'a') as log:
        log.write(f"{datetime.now()} - {e}\n")