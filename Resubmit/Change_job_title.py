import sys


def change_job_title(title):
    ns = ""
    with open("job.sh", 'r+') as f1:
        s = f1.read()
        s = s.split("\n")
        for idx,line in enumerate(s):
            if "job-name" in line:
                line = "#SBATCH --job-name=" + title
                s[idx] = line
        for line in s:
            ns = ns+line+"\n"
    with open("job.sh",'w') as f2:
        f2.write(ns)

if __name__ == "__main__":
    change_job_title(sys.argv[1])