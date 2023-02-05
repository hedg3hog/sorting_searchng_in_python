import random

from numpy import percentile
from sorting import *

l = [random.randint(0,100) for i in  range(10)]
print(l)
s = merge_sort(l)
print(s)
l.sort()
print(s == l)