def move(node):
    node=node.next
    return node

from LinkList import LinkList
a_list=LinkList([1,2,3,4])
p = a_list.head.next
print p
p = move(p)
print p

b=0
a=1 if b==0 else 3
print a 