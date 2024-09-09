def countSeniors(details) -> int:
    count = 0
    for i in details:
        v=int(i[11:13])
        if(v>60):
            count+=1
    return count
    
c=countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"])
print(c)
