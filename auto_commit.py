import os
import subprocess
from datetime import datetime, timedelta
import random

# Get the current working directory (repository path)
repo_path = os.getcwd()

# Function to execute git commands
def git_command(command):
    subprocess.call(command, shell=True)

# Number of commits to generate
total_commits = 100

# Current date
today = datetime.now()

# Generate commits with past dates
for i in range(total_commits):
    # Generate a random past date within the last year
    past_date = today - timedelta(days=random.randint(0, 365))
    
    # Create a commit message
    commit_message = f"Commit on {past_date.strftime('%Y-%m-%d %H:%M:%S')}"
    
    # Create or modify a file to make the commit unique
    with open("auto_commit.txt", "a") as f:
        f.write(f"{commit_message}\n")
    
    # Add changes to git
    git_command("git add .")
    
    # Make the commit with the generated past date
    git_command(f'git commit --date="{past_date.isoformat()}" -m "{commit_message}"')

# Push the commits to GitHub
git_command("git push origin main")
