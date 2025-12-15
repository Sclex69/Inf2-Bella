import numpy as np
arr = np.array([1, 2, 3, 2, 5, 4, 4, 3, 2])

def gaussian(x):
    c=x[0]+ x[2]+x[6]+ x[8]+2*x[1]+2*x[3]+2*x[5]+2*x[7]+4*x[4]
    c=c/16
    return c

def median(x):
    c=np.median(x)
    return c



y=gaussian(arr)
print(gaussian(arr))
print(median(arr))
