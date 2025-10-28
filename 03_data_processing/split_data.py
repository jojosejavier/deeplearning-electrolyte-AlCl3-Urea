import numpy as np
import dpdata

data = dpdata.MultiSystems.from_file(file_name="simulacion.traj", fmt="ase/structure")
system = data[0]
n = len(system)
n_val = int(0.2 * n)
val_indices = np.random.choice(n, size=n_val, replace=False)
train_indices = list(set(range(n)) - set(val_indices))
train_data = system.sub_system(train_indices)
val_data = system.sub_system(val_indices)
train_data.to_deepmd_npy('training_data')
val_data.to_deepmd_npy('validation_data')
