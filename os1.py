import os
import subprocess

from icecream import ic

current_dir = os.getcwd()
ic("Current dir: ", current_dir)

dir_contents = os.listdir(current_dir)
ic("Directory contents: ", dir_contents)

new_folder = "new_folder"
os.mkdir(new_folder)

renamed_folder = "renamed"
os.rename(new_folder, renamed_folder)
ic(f"Renamed original folder \"{new_folder}\" to \"{renamed_folder}\"")

cmd = "dir"
res = subprocess.run(cmd, shell=True, text=True, capture_output=True)
ic("CMD output: ", res.stdout)

ic("Path env var: ", os.environ.get("PATH"))