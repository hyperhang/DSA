def recursion(x):
    if x == 0:
        return 1
    res = res*recursion(x-1)