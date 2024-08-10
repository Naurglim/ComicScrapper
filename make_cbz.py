import zipfile
import pathlib
import os
import shutil

FOLDER = "C:/Comics/"

list_subfolders_with_paths = [f.path for f in os.scandir(FOLDER) if f.is_dir()]

for title_folder in list_subfolders_with_paths:
    issues_folders = [f.path for f in os.scandir(title_folder) if f.is_dir()]
    for issue_folder in issues_folders:
        directory = pathlib.Path(issue_folder)
        print(directory)
        with zipfile.ZipFile(issue_folder + ".cbz", "w", zipfile.ZIP_DEFLATED) as archive:
            for file_path in directory.iterdir():
                archive.write(file_path, arcname=file_path.name)
        shutil.rmtree(directory)
