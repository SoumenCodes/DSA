import subprocess
import time
from datetime import datetime

# Customized for your paths
REPO_PATH = r"C:\D Drive\DailyContributions\DSA-GITHUB\DSA"  # Your repository path
BRANCH = "main"  # Default branch (verify if different)
REMOTE = "origin"  # Standard remote name

def git_push():
    try:
        # Stage all changes
        subprocess.check_call(["git", "-C", REPO_PATH, "add", "."])
        
        # Check for changes
        status = subprocess.check_output(
            ["git", "-C", REPO_PATH, "status", "--porcelain"]
        ).decode().strip()

        if status:
            # Commit and push
            commit_message = f"DSA Practice: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.check_call(["git", "-C", REPO_PATH, "commit", "-m", commit_message])
            subprocess.check_call(["git", "-C", REPO_PATH, "push", REMOTE, BRANCH])
            print(f"✅ Pushed DSA updates at {datetime.now()}")
        else:
            print(f"⏩ No changes at {datetime.now()}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print(f"🚀 Starting DSA auto-pusher for {REPO_PATH}")
    while True:
        git_push()
        time.sleep(300)  # 5 minutes = 300 seconds