import bisect
a = [4,6,9,10,13]
x = 1
idx = bisect.bisect_left(a, x, lo=0, hi=len(a))
print(idx)