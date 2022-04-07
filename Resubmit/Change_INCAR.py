import sys


def change_incar(number1):
    ns = ""
    with open("INCAR", 'r+') as f1:
        s = f1.read()
        s = s.split("\n")
        for idx,line in enumerate(s):
            if "NSW" in line:
                line = "  NSW    =  "+number1+"          (Max ionic steps)"
                s[idx] = line
        for line in s:
            ns = ns+line+"\n"
    with open("INCAR",'w') as f2:
        f2.write(ns)

if __name__ == "__main__":
    change_incar(sys.argv[1])