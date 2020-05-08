import re
import os
import shutil
from pathlib import Path
import pyinputplus as pyip

def copy_files(file_ext, folder):
    # create new folder to copy* all the new stuff into
    new_folder_name = "ALL_" + file_ext + "_files"

    # check if the folder exists, if not, create one
    if not Path(folder + "/" + new_folder_name).exists():
        Path(folder + "/" + new_folder_name).mkdir()
    else:
        pass
    new_path = Path(folder + "/" + new_folder_name)

    # Walk through all folders, sub_folders, files
    # and copy anything w same extension into new folder
    for foldername, subfolders, files in os.walk(folder):
        for filename in files:
            if Path(filename).suffix == file_ext:
                print(f'Copying {filename} to {new_path}')
                full_path = os.path.join(foldername, filename)
                try:
                    shutil.copy(full_path, new_path)
                except:
                    continue


validExtension = re.compile(r"""
^(\.)  # must start with a dot
(.+)  #extension
""", re.VERBOSE)

extension = input("Please enter a file ext you would like to copy (.ext_name): ")
mo = validExtension.search(extension)
while mo is None:
    print("Invalid extension")
    extension = input("Please enter a file ext you would like to copy (.ext_name): ")
    mo = validExtension.search(extension)
p = Path.home() / 'Documents'
print(p)
path = pyip.inputFilepath()
copy_files(extension, path)
