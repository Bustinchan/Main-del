#FUCK C!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import os

dir_name = "C:/the/path/to/the/folder" #Place folder path here (WITH "/" NOT "\")
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".txt"): #change the text in the "" to the extension of the files you wish to delete (".txt",".exe",".pdf")
        os.remove(os.path.join(dir_name, item))
