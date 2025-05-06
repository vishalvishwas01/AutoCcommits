import os
import random
import time
from datetime import datetime
from pathlib import Path

repo_path = Path(".")
file_to_modify = repo_path / "njh.js"

if not file_to_modify.exists():
    file_to_modify.touch()

def perform_commits():
    num_commits = random.randint(3, 5)  # Keep low to avoid spam
    print(f"Performing {num_commits} commits...")

    for i in range(num_commits):
        with open(file_to_modify, "a") as file:
            file.write(f"Commit {i+1} at {datetime.now()}\n")

        os.system("git config user.name 'github-actions'")
        os.system("git config user.email 'github-actions@github.com'")
        os.system("git add .")
        os.system(f'git commit -m "Auto commit {i+1} at {datetime.now()}"')
        time.sleep(random.uniform(1, 2))  # Light delay

    os.system("git push")
    print(f"All commits pushed at {datetime.now()}.")

perform_commits()
