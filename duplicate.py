from tkinter.filedialog import askdirectory
from tkinter import Tk
import os
import hashlib
from pathlib import Path
import shutil
Tk().withdraw()
# file_path = askdirectory(title="Select a folder")
file_path = os.getcwd()
path = os.getcwd()+"\duplicate"
print(path)
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
			print(f"{file_path} has been deleted")
			# shutil.move(file_path,path , copy_function = path+str(file_path).split("test")[-1])
			# shutil.move(file_path,path+str(file_path).split("twitter")[-1] , copy_function =shutil.copytree )
			shutil.move(file_path,path, copy_function =shutil.copytree )
			# os.remove(file_path)
   			
			