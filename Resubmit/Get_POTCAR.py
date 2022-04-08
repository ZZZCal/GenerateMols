import sys, re, os


def get_element():
    with open("POSCAR", 'r+') as f1:
        line = f1.read()
        line = line.split("\n")
        element = line[0].split()
    return element

def write_POTCAR(ele):
    cwd = os.getcwd()
    potcar = ''
    path_pot = "path_to_potcar_file/pseudopotentials/PBE"
    folder = os.listdir(path_pot)
    for element in ele:
        for file in folder:
            if re.match(element, file):
                sub_directory = path_pot + "/" + element
                os.chdir(sub_directory)
                with open("POTCAR", 'r+') as file:
                    data = file.read()
        potcar += data
    os.chdir(cwd)
    with open("POTCAR", 'w') as file2:
        file2.write(potcar)


if __name__ == "__main__":
    record = get_element()
    write_POTCAR(record)




