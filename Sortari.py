import time
import random


def verifica(s):
    ok=1
    for i in range(0,len(s)-1):
        if s[i]>s[i+1]:
            ok=0
    if ok==0:
        print(" FAILED")
    else:
        print(" SUCCESS")

def Generator(n,maxim):
    rlist=[]
    for i in range(n):
        nrand=random.randint(0,maxim+1)
        rlist.append(nrand)
    return rlist


def quicksort(stanga, dreapta):
    global lis
    pivot = random.choice(lis[stanga:(dreapta+1)])
    s=stanga
    d=dreapta
    while s<=d:
        while lis[s]<pivot:
            s=s+1
        while lis[d]>pivot:
            d=d-1
        if s<=d:
            aux=lis[s]
            lis[s]=lis[d]
            lis[d]=aux
            s=s+1
            d=d-1
    if stanga<d:
        quicksort(stanga,d)
    if s<dreapta:
        quicksort(s,dreapta)

def bubblesort(lst):
    k=1
    while k>0:
        k=0
        for i in range(len(lst) - 1):
            if lst[i]>lst[i+1]:
                k = 1
                x=lst[i+1]
                lst[i+1]=lst[i]
                lst[i]=x
    return lst


def radixcount(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i=size-1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i=i- 1

    for i in range(0, size):
        array[i] = output[i]

def radix_sort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        radixcount(array, place)
        place *= 10

def countsort(v):
    fr=[0 for i in range(mil)]
    for i in v:
        fr[i]=fr[i]+1
    new=[]
    for i in range(mil):
        while fr[i]!=0:
            new.append(i)
            fr[i]=fr[i]-1
    return new


def interclasare(left, right):
    new = []
    x=0
    y=0
    while x < len(left) and y < len(right):
        if left[x]<right[y]:
            new.append(left[x])
            x=x+1
        else:
            new.append(right[y])
            y=y+1
    new.extend(left[x:])
    new.extend(right[y:])
    return new


def merge(lista):
    if len(lista)<=1:
        return lista
    else:
        mid=len(lista)//2
        left=merge(lista[:mid])
        right=merge(lista[mid:])
        return interclasare(left,right)

mil=10**6
lis=[]
n=int(input("Cate elemente?:"))
maxim= int(input("Elementul cel mai mare?:"))
lista=Generator(n,maxim)


print('Countsort: ')
if maxim<mil:
    start_time = time.time()
    sortata=countsort(lista)
    verifica(sortata)
    print(">%s secunde " % str(round((time.time() - start_time), 5)))
else:
    print(' FAILED, incearca cu elemente sub valoarea 1.000.000.')

print('\nBubble Sort: ')
if n<3000:
    start_time=time.time()
    sortata=bubblesort(lista)
    verifica(sortata)
    print(">%s secunde " % str(round((time.time() - start_time), 5)))
else:
    print(" FAILED, incearca cu sub 3.000 elemente.")
print('\n')


lis=lista[:]
start_time=time.time()
radix_sort(lis)
print('Radixsort: ')
verifica(lis)
print(">%s secunde " % str(round((time.time() - start_time), 5)))
print('\n')


start_time=time.time()
sortata=merge(lista)
print('Mergesort: ')
verifica(sortata)
print(">%s secunde " % str(round((time.time() - start_time), 5)))
print('\n')

lis=lista[:]
start_time=time.time()
quicksort(0,n-1)
print('Quicksort: ')
verifica(lis)
print(">%s secunde " % str(round((time.time() - start_time), 5)))
