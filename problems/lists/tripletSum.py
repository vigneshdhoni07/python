def findTriplet(ar, n, x) :
    #Your code goes here
    #return your answer
 c=0
 for i in range(n):
        for j in range(i+1,n):
          for k in range(j+1,n):
                if(ar[i]+ar[j]+ar[k]==x):
                    c+=1
 return c