
def get_total():
    with open("POSCAR", 'r+') as f1:
        data = f1.read()
        data = data.split("\n")
        for idx, line in enumerate(data):
            if "Direct" in line:
                count = idx
        number_list = data[count-1].split()
    number = 0
    for i in range(len(number_list)):
        number += int(number_list[i])
    return number

def write_new_INCAR(num):
    if (num % 2) == 0:
        number1 = number2 = int(num/2)
    else:
        number1 = int(num/2)
        number2 = number1+1

    ns = ""
    with open("INCAR", 'r+') as f1:
        s = f1.read()
        s = s.split("\n")
        for idx, line in enumerate(s):
            if "MAGMOM" in line:
                line = "   MAGMOM =" + str(number1) + "*1 " + str(number2) + "*0"
                s[idx] = line
        for line in s:
            ns = ns + line + "\n"
    with open("INCAR", 'w') as f2:
        f2.write(ns)


if __name__ == "__main__":
    num = get_total()
    write_new_INCAR(num)



