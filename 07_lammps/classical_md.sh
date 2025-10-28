#!/bin/bash
#SBATCH --partition=parallel
#SBATCH --time=24:00:00
#SBATCH --nodes=1                # Pedimos 1 nodo
#SBATCH --ntasks-per-node=64      # 64 procesos MPI por nodo
#SBATCH --job-name="Classical MD urea"
#SBATCH --output=test.out.%j
#SBATCH --mail-user=JOSE.ARCESOLORZANO@ucr.ac.cr
#SBATCH --mail-type=END,FAIL

cd /home/jose.arcesolorzano/md_urea/lammps

module purge
module load gnu12
module load openmpi4
module load lammps
source /home/jose.arcesolorzano/bin/miniforge3/etc/profile.d/conda.sh
conda activate deepmd

# Ejecutar LAMMPS con srun, usando todas las tareas asignadas
srun lmp -in in.lammps

