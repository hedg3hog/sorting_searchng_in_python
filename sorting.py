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

def heapify__(arr):
    n = len(arr)
    #print("n:", n)
    i = n // 2 -1
    if n == 2:
        i = 0
        if arr[i] < arr[i+1]:
            arr[i] ,arr[i+1] = arr[i+1], arr[i]

    while i >= 0:
        #print(i)
        if arr[i] < arr[i+1]:
            arr[i] ,arr[i+1] = arr[i+1], arr[i]
            i = i+1
        if n-i > 2 and arr[i] < arr[i+2]:
            arr[i] ,arr[i+2] = arr[i+2], arr[i]
            i = i + 1
        
        if i > n - 2:
            i =  n//2 -1
        else:
            i -= 1

    print(arr)
    return arr


def heapify(arr):
    arr = list(arr)
    n = len(arr)
    i = n//2 -1
    if n == 2:
        if arr[i] < arr[i+1]:
            return arr[::-1]
        return arr
    for i in range(i,-1,-1):
        if 2 * i + 1 < n and arr[i] < arr[2 * i + 1]:
            if 2 * i + 2 < n and arr[2*i + 1] < arr [2 * i + 2]:
                arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]
                #i = 2 * i + 2

                
            else:
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
                #i = 2 * i + 1
                
        elif 2 * i + 2 < n and arr[i] < arr [2 * i + 2]:
            arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]
            #i = 2 * i + 2
            

        #i -=1
    print(arr)
    return arr

def heap_sort(arr):
    arr = list(arr)
    s = list()
    for i in range(len(arr)):
        #print(arr)
        arr = heapify(arr)
        s.append(arr.pop(0))
    #s.append(arr.pop(0))
    if len(arr) > 0:
        arr.insert(0,arr.pop())
    return s[::-1]

        
        
        