list1 = [5,6,7,8]
list2 = [5,6,7,8]
print (list1)
print ( list1 == list2) 

list3 = list1

print ( list3 == list1)

list1.append(100)

print(list3) ## list3 will also change due to line 6 assignment....

list4 = list1.copy() # use copy command to overcome line 6 type of assignment

list1.append(500)

print(list1)
print(list4)
## for variables the working is a bit different....
a = 100
b = a
a = 500
print (a,b)


dir()