import os
from pathlib import Path
import shutil
import replace


def getOperation(directory_name, frag1):
    cwd = os.getcwd()
    directory = directory_name
    mol1 = frag1
    data1 = ""
    #
    if Path(directory).is_dir():
        sub_directory = cwd+"/"+directory
        os.chdir(sub_directory)
        if Path(mol1).is_dir():
            os.chdir(sub_directory+"/"+mol1)
            with open("operation.txt", 'r+') as file1:
                data1 = file1.read()
            os.chdir(sub_directory)
        else:
            print("Sorry, no such element marked with the number")
    else:
        print("no such color fragment in this molecule")
    os.chdir(cwd)
    return data1


def createSameTwo(ele1, ele2, operation_file):
    coorFile = "/Users/zhangzhenzhe/Desktop/Quasicrystal/mols/First-mole/Generazition/GenerateMols/original.cif"
    Coordinate = open(coorFile, 'rb')
    new_directory = ele1 + 'And' + ele2
    if Path(new_directory).is_dir():
        print("file has already been written")
    else:
        path = os.path.join(os.getcwd(), new_directory)
        os.makedirs(path)
        os.chdir(path)
        with open("operation.txt", 'w') as file3:
            file3.write(operation_file)
        original_file = open("original.cif", 'wb')
        shutil.copyfileobj(Coordinate, original_file)

        CIFfile = new_directory + '.cif'
        VASPFile = new_directory + '.vasp'
        replace.createFile("operation.txt", "original.cif", CIFfile)
        replace.createFile("operation.txt", "original.cif", VASPFile)


if __name__ == "__main__":
    print("Please enter each color fragment in order")
    x = [str(x) for x in input().split()]
    # rank by the alphabetical order
    x.sort()
    if len(x) == 2:
        print("Please choose the element and number in " + x[0])
        frag1 = str(input())
        print("Please choose the element and number in " + x[1])
        frag2 = str(input())
        operation_file = getOperation(x[0], frag1) + getOperation(x[1], frag2)
        if x[0] == x[1]:
            newsub_directory = os.getcwd() + "/" + x[0]
            os.chdir(newsub_directory)
            createSameTwo(frag1, frag2, operation_file)
        else:
            two_directory = os.getcwd() + "/" + x[0]+x[1]
            add_directory = x[0] + x[1]
            if Path(two_directory).is_dir():
                os.chdir(two_directory)
            else:
                new_path = os.path.join(os.getcwd(), add_directory)
                os.makedirs(new_path)
                os.chdir(new_path)
            createSameTwo(frag1, frag2, operation_file)





