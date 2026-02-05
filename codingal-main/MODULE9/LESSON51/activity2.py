#check if a file exits.
import os
print("checking the file exists or not.")
if os.path.exists('outsideFile2.txt'):
    print("the file exists.")
else:
    print("the file doesn't exists.")

# os.remove('outsideFile.txt')
os.rmdir('folderA')

