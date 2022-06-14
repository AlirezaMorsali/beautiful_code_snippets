from itertools import product
import numpy as np


dims = [8, 2, 3, 4]
x = np.random.randn(*dims)
print(x)
for i in product(*map(range, dims)):
    print(x[i])

