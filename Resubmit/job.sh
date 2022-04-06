#!/bin/bash
#SBATCH --time=6:00:00
#SBATCH --nodes=2
#SBATCH --tasks-per-node=64
#SBATCH --mem=255000M
#SBATCH --account=ctb-rzk 
#SBATCH --job-name=C2N
#SBATCH --error=_sub2.ste
#SBATCH --output=_sub2.stdo

module load VASP
srun vasp_std




