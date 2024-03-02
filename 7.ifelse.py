n1 = 100
n2 = 200
n3 = 300
n4 = 50

if n1 > n2:
    print("1 : n1 is larger than n2")
elif n1 < n3:
    print("2 : n1 is smaller than n3")
    #break
    if n1 < n4:
        print("3 : n1 is smaller than n2 as well")
    elif n1 > n4:
        print("4 : n4 is bigger than n4")
else:
    print('5 : n1 is smallest of all')


def func(py):
    return ['Python','Java']
     
lst = [2, 3, 4]
ret = func(lst);
print(ret)


if not 1:
    print("Welcome")
else:
    print("exit")
   
data = ""
while data:
    print("Data is not Empty")
else:
    print("Data is Empty")

print(dir(dict))

strval = 'Hello world'

print(strval.capitalize())
print(strval.lower())
print(strval.removeprefix('He'))
print(strval.removesuffix('ld'))
print(strval.rjust(10,'_'))
print(strval.partition('l'))
print(strval.rpartition('W'))
print(strval.title())
print(strval.upper())
print(strval.zfill(12))

for i in dir(list):
    print (i, sep = ":")