import random
from sorting import *

l = [random.randint(0,100) for i in  range(16)]
print("gen done")
s = heap_sort(l)
print("heap done")
print(s)
l.sort()
print(s == l)
