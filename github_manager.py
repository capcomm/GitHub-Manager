import os
import subprocess

GITHUB_REPO = "git@github.com:capcomm/FidelityPortfolioManager.git"

TRACKED_FILES = ["backend", "scripts", "README.md", "requirements.txt"]

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if output:
        print(output.decode())
    if error:
        print("Error:", error.decode())

def commit_and_push():
    for file in TRACKED_FILES:
        run_command(f"git add {file}")
    commit_message = input("Enter commit message: ")
    run_command(f'git commit -m "{commit_message}"')
    run_command("git push origin main")

commit_and_push()
