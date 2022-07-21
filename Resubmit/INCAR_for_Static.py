import sys


def change_incar():
    ns = ""
    with open("INCAR", 'r+') as f1:
        s = f1.read()
        s = s.split("\n")
        for idx, line in enumerate(s):
            if "NSW" in line:
                line = ""
                s[idx] = line
            if "Ionic Relaxation" in line:
                line = ""
                s[idx] = line
            if "IBRION" in line:
                line = ""
                s[idx] = line
            if "ISIF" in line:
                line = ""
                s[idx] = line
            if "EDIFFG" in line:
                line = ""
                s[idx] = line
        for line in s:
            ns = ns+line+"\n"
    with open("INCAR",'w') as f2:
        f2.write(ns)

if __name__ == "__main__":
    change_incar()