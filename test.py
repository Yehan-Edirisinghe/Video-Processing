import numpy as np


def func(x):

    x[0] = 0
    x[1] = 2

a = np.ones(5)

func(a)

print(a)