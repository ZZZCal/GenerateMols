import sys


def change_incar():
    ns = ""
    with open("INCAR", 'r+') as f1:
        s = f1.read()
        s = s.split("\n")
        for idx,line in enumerate(s):
            if "ICHARG" in line:
                line = "ICHARG =  11          (Non-self-consistent: GGA/LDA band structures)"
                s[idx] = line
            if "ALGO" in line:
                line = "IALGO = 48"
                s[idx] = line
            if "NPAR" in line:
                line = "NPAR   = 4           (Max is no. nodes; don't set for hybrids)"
                s[idx] = line
        for line in s:
            ns = ns+line+"\n"
    with open("INCAR",'w') as f2:
        f2.write(ns)

if __name__ == "__main__":
    change_incar()