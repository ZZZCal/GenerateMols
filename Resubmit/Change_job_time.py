import sys


def change_job_time(hour, min):
    ns = ""
    with open("job.sh", 'r+') as f1:
        s = f1.read()
        s = s.split("\n")
        for idx,line in enumerate(s):
            if "time" in line:
                line = "#SBATCH --time="+hour+":"+min+":00"
                s[idx] = line
        for line in s:
            ns = ns+line+"\n"
    with open("job.sh",'w') as f2:
        f2.write(ns)

if __name__ == "__main__":
    change_job_time(sys.argv[1], sys.argv[2])