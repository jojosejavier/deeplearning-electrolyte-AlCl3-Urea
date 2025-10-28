#!/bin/bash
#SBATCH --account=c5071
#SBATCH --partition=gpu
#SBATCH --qos=gpu
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --job-name="Training-500Urea"
#SBATCH --output=dp.out.%j

module purge
module load gnu12
module load openmpi4

source $HOME/bin/miniforge3/etc/profile.d/conda.sh
conda activate deepmd

cd /home/jose.arcesolorzano/md_urea/500/Training/

dp train input.json
