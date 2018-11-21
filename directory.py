import os
path=input("enter folder path")
l=os.listdir(path)
print("folder names:",l)
for x in l:
    if(os.path.isdir(x)):
        print("subfolder names",os.listdir(x))
