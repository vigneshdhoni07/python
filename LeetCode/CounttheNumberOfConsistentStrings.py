def countConsistentStrings(allowed: str, words) -> int:
    count=len(words)
    allowedObj={}
    for i in allowed:
        if allowedObj.get(i) is None:
            allowedObj[i]=i
    for j in words:
        for k in j:
            if allowedObj.get(k) is None:
                count-=1
                break
    return count

    

# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# allowed = "abc"
# words = ["a","b","c","ab","ac","bc","abc"]
allowed = "cad" 
words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(countConsistentStrings(allowed,words))
