import matplotlib.pyplot as plt
import numpy as np
int_nums=np.random.random(100)
fig=plt.figure()
plt.hist(int_nums)
plt.grid(True)
plt.show()