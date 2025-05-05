# main.py
import os
import random
import time
from datetime import datetime
from pathlib import Path

# Set your repo path (no need for full path in Railway, just local dir)
repo_path = Path(".")
file_to_modify = "njh.js"

def perform_commits():
    num_commits = random.randint(25, 35)
    print(f"Performing {num_commits} commits...")

    for i in range(num_commits):
        with open(file_to_modify, "a") as file:
            file.write(f"Commit {i+1} at {datetime.now()}\n")

        os.system("git add .")
        os.system(f'git commit -m "Auto commit {i+1} at {datetime.now()}"')
        time.sleep(random.uniform(2, 5))  # Delay between commits

    os.system("git push origin main")
    print(f"All {num_commits} commits pushed at {datetime.now()}.")

perform_commits()
