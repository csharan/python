print (11/3) # this will show float values
print (11//3) # this will show integer values, anything after "." will be ignored..
print (3//4) # this will show integer values, anything after "." will be ignored..
print (11%3) # gives the reminder values...
print (3**5) ## ** is for exponent values
print(1 ** 6 // 3)

## dictionay operations
a = {"name" : "sharan", "age" : "44", "city" : "chennai"}
b = {"name" : "sharan", "age" : "44", "city" : "chennai"}
print(a == b)
c = {"name" : "preethi", "age" : "37", "city" : "cbe","education":"bsc"}
d = a.update(c)
print(d)

#dict1 = {'Name':'Samuel'}
#dict2 = {'Age': 20}
#dict3 = dict1 + dict2 ## does not work...
#print(dict3)

## print operations
#end = 'end=#'

for i in range (0,5):
    print (i, end = "$") ## end parameter basically ends the line and prints next to next

for ch in "Books":
    print(ch,end=" ")

## Tuple operations

#val = ("hi","hello","bye") # remember, tuples cannot be popped!!!
#val.pop() ## will lead to error...

print("\n") ## add a new line..

# string comparisons...
s1 = "Hello"
s2 = "hello"
print("the values of comparison is :", s1 == s2.title(), "\n")

city1 = "New York"
city2 = "New York"
print(city1 is city2)

print(bool(0) + 5)
print(bool(1) + 5)


a = 10
if True:
    print('TRUE!')
print(a)

def reduce(a):
    while a > 3:
        a = a - 1
    else:
        print(a)
a=4
reduce(a)

def swap(a, b):
    a, b = b, a
    return (a, b)
     
a = "Python2"
b = "Python3"
a, b = swap(a, b)
print(a, b)

a, b, c, d = 4, 2.5, "Sandeep", True
print(a, b, c, d)


a = 1
b = 1
print(a^b)

def num(x = 1, y = 3):
    x = x + y
    y += 1
    print(x, y)

num(y = 3, x = 1)

print("I", "am", "not", "a", "doctor", sep="#")

print = "Hi"
print (print)

x = 10.5
y = "ONE"
print(int(x))
#print(int(y))

str = 'coding'
if len(str)> 3:
    print("coding")
    if len(str) <= 8:
        print("python")

a= [1,2,3,4,5]
print(a.index(3))

tupl = (1, 2,3,4,5)
print(tupl[-3])

list = ['sam', 'jam', 'mam', 'dam']
i = 0
while True:
    print(list[i])
    if (list[i] == 'jam'):
        print('jam')
        break
    i += 1

pet="dog"
for i in range(0,len(pet)):
    print(pet[i])

def func(id1 = 76, id2 = 42, id3 = 90):
   print(id1, id3, id2)

func(id3 = 87, 78, 98)


    num1 = 8
    num2 = 10
    num3 = 12
    if num1 < num2:
       if num1 < num3:
           print('smallest is:', num1)
    elif num2 < num1:
       if num2 < num3:
           print('smallest is:', num2)
    elif num3 < num1:
       if num3 < num2:
           print('smallest is:', num3)
    else:
       print('else')

for ch in "california":
    print(ch, end = "@")


def swap(num1, num2):
    temp = num1;
    num1 = num2;
    num2 = temp;

num1 = (2)
num2 = (5)
swap(num1, num2)
print(num1 , num2)

print(end='',sep='@@')

print("I love\\nPython.")
print("I love\\Python.")

initial = 1
while initial < 3:
    initial += 1
    print(initial)
    break
else:
    print("Break")

if not 1:
    print("Welcome")
else:
    print("exit")

list = [i for i in range(4)]
print(list)

data = ""
while data:
    print("Data is not Empty")
else:
    print("Data is Empty")


def func(lst):
    lst = [1,2,3]
    return lst
     
lst = [4,5,6]
ret = func(lst)
print(lst, ret)

name, phone, location = "Pihu Gupta", 9018273645, "Ranchi"
print(name, phone, location, sep="**")

def fun(ndf, df = 6):
    return df/ndf 
print(fun(6,4))

## variable assignments...
a = b = 5
print (a, b)

b = 10
print (a, b)

a, b = 20,30
print(a,b)