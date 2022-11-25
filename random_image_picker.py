import os
import random 
path="G:\\Input\\girls"
print(len(path))
files=os.listdir(path)
d=random.choice(files)
print(d)
# os.startfile(d)