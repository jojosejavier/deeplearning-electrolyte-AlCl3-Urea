from ase.io import read, write

frames = read("pw.out", format="espresso-out", index=":")
write("simulacion.traj", frames, format="traj")
