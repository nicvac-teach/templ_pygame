import os
import subprocess

# Repository URL and folder name
repo_url = "https://github.com/nicvac-teach/lezioni_pygame.git"
repo_folder = "lezioni_pygame"

# Check if the repository folder already exists
if os.path.exists(repo_folder):
    print(f"Il repository '{repo_folder}' è già presente. Aggiornamento in corso...")
    subprocess.run(["git", "-C", repo_folder, "pull"])
else:
    # Clone the repository
    subprocess.run(["git", "clone", repo_url])
    
print("Lezioni aggiornate!")
