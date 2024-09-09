ar=[13,4,9,5,3]

def insertionSort(ar):
    for i in range(0,len(ar)):
        min=i
        for j in range(i+1,len(ar)):
            if(ar[j]<ar[min]):
                min=j
        ar[min],ar[i]=ar[i],ar[min]
            
insertionSort(ar)
print(ar)