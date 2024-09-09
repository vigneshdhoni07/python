class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

node1=Node(3)
node2=Node(4)
node1.next=node2

# print(node1.data)
# print(node2.data)
# print(node1.next.data)
# print(node1.next)
# print(node2)

def takeInput():
    li=[int (i) for i in input("Enter Input").split()]
    head=None
    curr=None
    for i in li:
        node=Node(i)
        if head is None:
            head=node
        else:
            curr.next=node
        curr=node
        
    return head

list=takeInput()
def printInput(head):
    while head is not None:
        print(head.data,end="-->")
        head=head.next
    print("None")
    
printInput(list)

newNode=Node(int(input("Enter NewNode:")))
ind=int(input("Enter Index:"))

def insertEleRecurs(head,curr,i,newNode,c):
    if(i==0):
        newNode.next=head
        return newNode
    if curr is None:
        return head
    if(i-1==c):
        temp=curr.next
        curr.next=newNode
        newNode.next=temp
        return head
    insertEleRecurs(head,curr.next,i,newNode,c+1)
    return head

newHeadRecursive=insertEleRecurs(list,list,ind,newNode,0)
printInput(newHeadRecursive)
    
        
    