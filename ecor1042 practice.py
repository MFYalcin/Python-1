'''
a = {1,2,3,3,3,1}
a_set = set()
a_count = 0
for x in a:
    a_set.add(x)

for x in a_set:
    a_count += x
print(a_count)
##
a_str = 'Hello'
a_list = [3,5,a_str]
item = a_list[1]
for item in a_list:
    print(item
##

d = {111: "Tom", 222:"Dick", 333:"Harry"}
items = d.items()
for item in items:
    print(item)
    #tuples

##
def selection_sort(d):
    for i in range(len(d)-1,0,-1):
        for j in range(i):
            if d[j]>d[j+1]:
               d[j+1],d[j] = d[j],d[j+1]
d = [5,3,8,6,7,2]
selection_sort(d)
print(d)

##


def insertion_sort(arr):
   for i in range(1,len(arr)):
      j = i
      while arr[j-1] > arr[j] and j>0:
         arr[j-1], arr[j] = arr[j], arr[j-1]
         j -= 1
arr = [2,6,5,1,3,4]
insertion_sort(arr)
print(arr)
##

def bubble_sort(b):
    for i in range(len(b)-1,0,-1):
        for j in range(i):
            if b[j] > b[i]:
                b[j], b[i] = b[i],b[j]
b = [1,4,5,2,3,9,12]
bubble_sort(b)
print(b)
##


def selection_sort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
a = [1,2,7,8,9,4,5,6]
selection_sort(a)
print(a)
##


def insertion_sort(c):
    for i in range(1,len(c)):
        j = i
        while c[j-1] > c[j] and j>0:
            c[j-1],c[j] = c[j],c[j-1]
            j-= 1
            
c = [1,5,6,2,3,15]
insertion_sort(c)
print(c)
            
##


def merge_sort(a):
    if len(a)>1:
        mid = len(a)//2
        l = a[:mid]
        r= a[mid:]
       
        merge_sort(l)
        merge_sort(r)
        
        i = 0
        j = 0
        k = 0
        
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                a[k] = l[i]
                i+=1
            else:
                a[k] = r[j]
                j+=1
            k+=1
            
        while i<len(l):
            a[k] = l[i]
            i+=1
        while j<len(r):
            a[k] = r[j]
            j+=1
        k+=1
a = [1,4,6,3,2,10]
merge_sort(a)
print(a)

##


d = {'a':1,'b':2,'c':3}
del d['a']
print(d)

##
'''
lst = [[1,2,3],[4,5]]
sum = 0
for row in range(len(lst)):
    for col in range((len(lst[row]))):
        sum += lst[row][col]
print((lst[row][col]))




