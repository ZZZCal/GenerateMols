import re
import sys
from ase.build import sort
from ase.io import read,write

def createFile(coordinateFile, operationFile, newFile):
    slab = read(coordinateFile, format='cif')
    operation = []
    data = []
    with open(operationFile, 'r') as fx:
        for lines in fx:
            line = re.split('\s+', lines)
            line = [x for x in line if x != '']
            operation.append(line)

    with open(coordinateFile, 'r') as fy:
        for lines in fy:
            line = re.split('\s+', lines)
            line = [x for x in line if x != '']
            if len(line) > 7:
                data.append(line)

    for goal in range(len(operation)):
        for element in range(len(data)):
            if re.fullmatch(operation[goal][0], data[element][0]):
                if re.search("replace", operation[goal][1]):
                    slab[element].symbol = operation[goal][2]

    for delete_goal in range(len(operation)):
        for delete_element in range(len(data), 0, -1):
            if re.fullmatch(operation[delete_goal][0], data[delete_element-1][0]):
                if re.search("delete", operation[delete_goal][1]):
                    slab.pop(delete_element-1)

    slab = sort(slab)
    write(newFile, slab, format='cif')

if __name__ == "__main__":
    # print("Please type three file: (1)coordinate file (2)operation file (3)new file name")
    createFile(sys.argv[1], sys.argv[2], sys.argv[3])








