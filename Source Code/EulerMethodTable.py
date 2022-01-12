import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# RECURSIVE EULER METHOD
def euler(y0, x0, h, n):
    return get_yn(y0, x0-h, h, n)

def get_yn(y0, x0, h, n):
    if(n == 0):
        return y0
    else:
        x0 = x0 + h
        n = n - 1
        yn = get_yn(y0, x0, h, n)
        return round((yn + h * F(yn, x0)), 4);

# END EULER METHOD

def F(y0, x0):
    return y0

def f(y, x):
    return np.exp(x);


def getTable(h):
    rows, cols = (0, 3)
    infoTable = [[0]*cols]*rows
    infoTable.insert(0,['xi (h = ' + str(h) + ')', 'y-exact (h = ' + str(h) + ')', 'y-num (h = ' + str(h) + ')'])

    i = 1
    x = 0
    while(x <= 1):
        infoTable.insert(i, [x, f(0, x), euler(1, 0, h, i)])
        x = round(x + h,2)
        i = i + 1
    print(tabulate(infoTable, headers = 'firstrow', tablefmt = 'fancy_grid'))

print('\nTable for h = 0.1')
getTable(0.1) # Table for h = 0.1
print("\n\nTable for h = 0.05")
getTable(0.05) # Table for h = 0.05


