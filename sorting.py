import enum
import imp
from time import sleep

from numpy import append

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
    
def merge_sort(liste:list):
    if len(liste) > 2:
        #print("sorting",liste[:len(liste)//2],liste[len(liste)//2:])
        return sorted_merge(merge_sort(liste[:len(liste)//2]),merge_sort(liste[len(liste)//2:]))
    elif len(liste) == 2:
        return sorted_merge([liste[0]],[liste[1]])
    else:
        #print(1,liste)
        return liste

def sorted_merge(left:list, right:list):
    merged = list()
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j +=1
        
    merged += left[i:] 
    merged += right[j:]
    print("merged",left, right, "to", merged)
    return merged

