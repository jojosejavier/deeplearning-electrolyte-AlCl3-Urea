from ase.io import read, write
from ase.data import atomic_masses
import numpy as np
import sys

in_xyz  = sys.argv[1]
outdat  = sys.argv[2] if len(sys.argv) > 2 else "data.lammps"

atoms = read(in_xyz)  
# Si no tiene celda y quieres caja periódica fija, descomenta:
# atoms.set_cell([10.0, 10.0, 10.0])   # en Å
# atoms.set_pbc([True, True, True])

# Asegura que las masas queden en el data (ASE las infiere por símbolo)
symbols = atoms.get_chemical_symbols()
unique = sorted(set(symbols), key=symbols.index)  # orden por primera aparición
masses = [atomic_masses[atoms[i].number] for i in [symbols.index(s) for s in unique]]


# Escribe en formato LAMMPS (atom_style = atomic por defecto)
write(outdat, atoms, format="lammps-data", units="metal", atom_style="atomic")
print(f"Escrito: {outdat}. Tipos: {unique}")


#python xyz_to_lammps.py interface__reduced_centered.xyz data_reduced.lammps
