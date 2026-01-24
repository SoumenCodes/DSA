import subprocess
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"update_{timestamp}.txt"

try:
    subprocess.run(['git', 'status'], check=True)

    with open(filename, 'w') as f:
        f.write(f"Auto-commit at {timestamp}\n")

    subprocess.run(['git', 'add', filename], check=True)
    subprocess.run(['git', 'commit', '-m', f'Add {filename}'], check=True)
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)

    print(f"✅ Successfully pushed {filename} to GitHub!")

except subprocess.CalledProcessError as e:
    print("❌ Git command failed")
    print(e)
