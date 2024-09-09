ar=[56,32,21,12,34,67,78,65]

def bubbleSort(ar):
    for i in range(0,len(ar)):
        for j in range (0,len(ar)-i-1):
            if(ar[j]>ar[j+1]):
                ar[j],ar[j+1]=ar[j+1],ar[j]
              
bubbleSort(ar)
print(ar)