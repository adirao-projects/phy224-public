import numpy as np


def digits(n):
    if n==0:
        return 1
    else:
        return abs(int(np.log10(n)))+1

def round(n, d):
    if n==0:
        return
    