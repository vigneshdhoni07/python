ar=['c','e','a','y','d','h','f']

def insertionSort(ar:list[chr],)->None:
    for i in range(0,len(ar)):
        min=i
        for j in range(i+1,len(ar)):
            if(ord(ar[j])<ord(ar[min])):
                min=j
        temp=ar[i]
        ar[i]=ar[min]
        ar[min]=temp
            
insertionSort(ar)
print(ar)