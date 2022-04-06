import sys


def change_job_time(number1, number2):
    ns = ""
    with open("job.sh", 'r+') as f1:
        s = f1.read()
        s = s.split("\n")
        for idx,line in enumerate(s):
            if "time" in line:
                line = line.replace(number1, number2)
                s[idx] = line
        for line in s:
            ns = ns+line+"\n"
    with open("job.sh",'w') as f2:
        f2.write(ns)

if __name__ == "__main__":
    change_job_time(sys.argv[1], sys.argv[2])