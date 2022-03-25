import re
import sys

from ase import Atoms
from ase.build import sort
from ase.io import read,write


def createFile(coordinateFile, operationFile, newFile):
    slab = read(coordinateFile, format='cif')
    operation = []
    data = []
    # put operations in list
    with open(operationFile, 'r') as fx:
        for lines in fx:
            line = re.split('\s+', lines)
            line = [x for x in line if x != '']
            operation.append(line)

    # put only element in list
    with open(coordinateFile, 'r') as fy:
        for lines in fy:
            line = re.split('\s+', lines)
            line = [x for x in line if x != '']
            if len(line) > 7:
                data.append(line)

    # find all operations except delet, further operation as long as it did not delete atoms can put here
    for goal in range(len(operation)):
        for element in range(len(data)):
            if re.fullmatch(operation[goal][0], data[element][0]):
                if re.search("replace", operation[goal][1]):
                    slab[element].symbol = operation[goal][2]
                if re.search("delete", operation[goal][1]):
                    slab[element].symbol = "Pr"

    # delete all 'Pr' elements
    slab = sort(slab)
    new_list = Atoms([i for i in slab if i.symbol != "Pr"])
    new_list.cell = slab.cell
    new_list.pbc = slab.pbc
    write(newFile, new_list, format = "cif")

    # delete atoms from the end of list, in case of delete wrong atoms
    # for delete_goal in range(len(operation)):
    #     for delete_element in range(len(data), 0, -1):
    #         if re.fullmatch(operation[delete_goal][0], data[delete_element-1][0]):
    #             if re.search("delete", operation[delete_goal][1]):
    #                 slab.pop(delete_element-1)
    # for atom in slab:
    #     if atom.symbol == "Pr" :
    #         slab.pop(atom.number)

    # sort element by chemical symbol, which is easier for VASP calculation potential file creation


if __name__ == "__main__":
    # print("Please type three file: (1)coordinate file (2)operation file (3)new file name")
    createFile(sys.argv[1], sys.argv[2], sys.argv[3])
    # createFile("test.cif", "operation.txt", "newFile.cif")















