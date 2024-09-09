a={1:2,2:4,"li":[1,2,3],"di":{1:3,3:5}}
print(a[1])
print(a["li"])
# print(a["list"]) #Error as key list is not in dictionary
print(a.get(1))
print(a.get("li"))
print(a.get("list"))#None #No error will be there as we use get methods
print(a.get("list",10))# If key is not available it will return second parameter #10
print(a.get("li",10))#[1,2,3]
print(a.keys())#dict_keys([1, 2, 'li', 'di'])
print(a.values())#dict_values([2, 4, [1, 2, 3], {1: 3, 3: 5}])
print(a.items())#dict_items([(1, 2), (2, 4), ('li', [1, 2, 3]), ('di', {1: 3, 3: 5})])

for i in a:
    print(i)# prints key
    print(a[i])#prints value

for i in a.values():
    print(i)# print values
    
# boolean
    print(1 in a)
    print(5 in a)