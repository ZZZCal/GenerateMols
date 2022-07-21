import sys


def change_incar():
    ns = ""
    with open("INCAR", 'r+') as f1:
        s = f1.read()
        s = s.split("\n")
        for idx,line in enumerate(s):
            if "NSW" in line:
                line = "  NSW = 1   "
                s[idx] = line
            if "NUPDOWN" in line:
                line = "  NUPDOWN = 2   "
                s[idx] = line
        for line in s:
            ns = ns+line+"\n"
    with open("INCAR",'w') as f2:
        f2.write(ns)

if __name__ == "__main__":
    change_incar()