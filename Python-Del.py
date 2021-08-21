#FUCK C!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import os

dir_name = "C:/Users/danie/Desktop/Coding/Bustin" #Place folder path here (WITH "/" NOT "\")
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".txt"):
        os.remove(os.path.join(dir_name, item))