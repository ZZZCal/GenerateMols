import sys


def change_job_cpus(nodes, cpus):
    ns = ""
    with open("job.sh", 'r+') as f1:
        s = f1.read()
        s = s.split("\n")
        for idx,line in enumerate(s):
            if "nodes" in line:
                line = "#SBATCH --nodes=" + nodes
                s[idx] = line
            if "tasks-per-node" in line:
                line = "#SBATCH --tasks-per-node=" + cpus
                s[idx] = line
            if "mem" in line:
                line = "#SBATCH --mem=0"
                s[idx] = line
        for line in s:
            ns = ns+line+"\n"
    with open("job.sh",'w') as f2:
        f2.write(ns)

if __name__ == "__main__":
    change_job_cpus(sys.argv[1], sys.argv[2])