import matplotlib.pyplot as plt
import numpy as np

a = [i**2 for i in range(10)]

d = {'a': 10, 'b': 20, 'c': 30}

a = [(k, v) for k, v in d.items()]

labels = ['a', 'b']
a = [d[key] for key in labels]

print(a)
# plt.show()