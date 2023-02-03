import imp
from time import sleep

def quick_sort(liste:list):
    if len(liste) < 2:
        return liste

    p = liste[-1]
    g = list()
    k = list()
    for i in liste[:-1]:
        if i > p:
            g.append(i)
        else:
            k.append(i)
    print(k,p,g)
    print()
    sleep(1)
    return quick_sort(k)+ [p,] + quick_sort(g)
    
