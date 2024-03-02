for ch in "california":
    print(ch) ## each time print is considered a new one and printed in separate line...

list1 = ["a","b","c","d","e"]
for i in list1:
    print (i) ## each time print is considered a new one and printed in separate line...

for ch in "california":
    print(ch, end = "@") ## prints in same line...

for num in range(3, 12, 2):
    print(num, end = ",")

# list comprehensions....
lst = [3,6,8,9]
lst1 = []
number1 = 0

#for number in lst:
#    lst1.append(number **2)
#print(lst1, number)

lst1 = ([number **2 for number in lst])
print(lst1)

expressions = ["lol","rofl","lmao"]
#print([expression.upper() for expression in expressions])
exp = [expression.upper() for expression in expressions]
print(exp)

donuts = ['boston cream','jelly','vanilla cream','glazed','chocolate cream']
donuts1 = [d for d in donuts]
print (donuts1)

donuts = ['boston cream','jelly','vanilla cream','glazed','chocolate cream']
donuts1 = [d for d in donuts]
print (donuts1) 
donuts1 = [d for d in donuts if "cream" not in d]
print(donuts1)
donuts = ['boston cream','jelly','vanilla cream','glazed','chocolate cream']
donuts1 = [len(d) for d in donuts]
print(donuts1)

measure = [[2,4] for i in range (3,5)]
print(measure)

measure = [0 for i in range (3)]
print(measure)

def recfun ():
    i = 0
    print ("Hello")
    while i < 5:
        print ("Hello-2")
        i += 1
        recfun

recfun()

def process(data):
    #data = [1,2,3]
    return data [-2]

#print(process(9))
measurements = [0 for i in range (3)]
process(measurements)
#print(measurements)
print(measurements[-2])

#########################################################
a = [1,2,3]
d = [4,5,6]
b = 200

def process_list():
    a.pop(1) ## updates the list outside the function...
    b = 900 ## does not update the var outside the function
    d = [7,8,9] ## does not update the list outside the function...
    return a

print(process_list())
print(a)
print (b)
print (d)

def combine (width, height = 10, depth = 0, is_3d = False):
    return (is_3d, width, height, depth)

print(combine(height = 1, width = 2)[3])