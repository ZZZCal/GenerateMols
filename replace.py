import sys
import re
from ase import io
from ase.io import read,write

def operation_on_file(OperationFile, CoordinateFile):
    title = []
    operation = []
    data = []
    with open("operation.txt", 'r') as fx:
        for lines in fx:
            line = re.split('\s+', lines)
            line = [x for x in line if x != '']
            operation.append(line)

    with open("test.cif", 'r') as fy:
        for lines in fy:
            line = re.split('\s+', lines)
            line = [x for x in line if x != '']
            if 7 < len(line) < 10:
                data.append(line)
            else:
                title.append(line)
    for i in range(len(operation)):
        for j in range(len(data)):
            # if the label has one digit
            if len(operation[i][0]) == 2 and len(data[j][0]) == 2:
                if data[j][0][0] == operation[i][0][0] and data[j][0][1] == operation[i][0][1]:
                    if operation[i][1] == "replace":
                        data[j][0] = operation[i][2] + data[j][0][1]
                        data[j][-1] = data[j][0][0]
                    elif operation[i][1] == "delete":
                        data[j][0] = "Del"
                    # more operation can be added
            # if the label has two digits
            elif len(operation[i][0]) == 3 and len(data[j][0]) == 3:
                if data[j][0][0] == operation[i][0][0] and (data[j][0][1] + data[j][0][2]) == (operation[i][0][1] + operation[i][0][2]):
                    if operation[i][1] == "replace":
                        data[j][0] = operation[i][2] + data[j][0][1]
                        data[j][-1] = data[j][0][0]
                    elif operation[i][1] == "delete":
                        data[j][0] = "Del"
                    # more operation can be added
    return title, data

def write_ciffile(filename, title, data):

    # count how many atoms are deleted (only used in xyz file)
    # count = 0
    # for i in range(len(data)):
    #     if data[i][0] == "Del":
    #         count += 1
    # title[0][0] = str(int(title[0][0]) - count)

    # write cif file title:
    with open(filename, 'w') as f:
        for line in title:
            line = re.sub("[][\',]", "", ("%s\n" % line))
            f.write(line)

    # write full cif file:
    with open(filename, 'a') as fnew:
        for lineAdd in data:
            # del lineAdd[-1]
            if lineAdd[0] != "Del":
                lineAdd = re.sub("[][\',]", "", ("%s\n" % lineAdd))
                fnew.write(lineAdd)
    # slab = read(filename, format='xyz')
    # write(filename, slab, format='cif')


if __name__ == "__main__":
    # title, data = operation_on_file("operation.txt", "test.cif")
    # write_ciffile("newFile.cif", title, data)

    title, data = operation_on_file(sys.argv[1], sys.argv[2])
    write_ciffile(sys.argv[3], title, data)










