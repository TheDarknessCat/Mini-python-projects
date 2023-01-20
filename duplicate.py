###move duplicate images to duplicate folder###
from tkinter.filedialog import askdirectory
from tkinter import Tk
import os
import hashlib
from pathlib import Path
import shutil
Tk().withdraw()
file_path = os.getcwd()
path = os.getcwd()+"\duplicate"
list_of_files = os.walk(file_path)
unique_files = dict()
os.makedirs(path)
for root, folders,files in list_of_files:
	for file in files:
		file_path = Path(os.path.join(root, file))
		Hash_file = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
		if Hash_file not in unique_files:
			unique_files[Hash_file] = file_path
		else:
			shutil.move(file_path,path, copy_function =shutil.copytree )

   			
			
