words=input("Enter the Sentence:").split(" ")
k=int(input("Enter the Frequency:"))

def wordsWithFreq(sentence,f):
    freq={}
    NoOfWords=[]
    for i in sentence:
        freq[i]=freq.get(i,0)+1
        # if(freq.get(i) == None):
        #     freq[i]=1
        # else:
        #     freq[i]=freq[i]+1
    for v in freq:
        if(freq[v]==f):
            NoOfWords.append(v)
    return NoOfWords
    
print(wordsWithFreq(words,k))