import os
import re


def mv_contcar():
    with open("CONTCAR", 'r+') as f1:
        file1 = f1.read()

    with open("POSCAR", 'w') as f2:
        f2.write(file1)




if __name__ == "__main__":
    path = os.getcwd()
    folder = os.listdir(path)
    for file in folder:
        if file.endswith('.stdo'):
            checkfile = open(os.path.join(path, file), 'r+')
            check = checkfile.read()
    if re.search("reached required accuracy", check):
        mv_contcar()
    else:
        print(path)



