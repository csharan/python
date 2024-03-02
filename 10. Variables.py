## variable assignments...
a = b = 5
print (a, b)

b = 10
print (a, b)

a, b ,c= 20,30,50
print(a,b,c)

def adds (a,b):
    print(a+b) ## this will be printed....
    return a + b
    print(a+b) ## this line will not execute as fn ends with return...

print (adds(5,10))


def adds (a = 10,b = 8):
    return a + b

#result = adds(a = 9 ,100) ## leads to error
#print(result)

result = adds(a = 9) ## works
print(result)

print(type(None))

# functions without any explicit return will return "None"

def adds (a = 10,b = 8):
    print (a + b)

print(adds()) # returns "None"

value = 95

if 90 < value < 100 :
    print ("this works")

## using lists in while loop...
meals = ['lunch','bfast','dinner']
print (meals[2][1]) ## look how the position works...
print (meals[-2][2]) ## look how the position works...
print (meals[-2][-2]) ## does not work...

while "lunch" in meals :
    print ("you have lunch today")
    meals.remove("lunch")

print(meals)

print ("prog"[3:1]) ## 6th item not included...and starts with 0

print (["lunch", "bfast"] in ['lunch','bfast','dinner']) ## evaluTES TO FLASE

print (["lunch", "bfast"] in [['lunch','bfast'],'dinner']) ## evaluTES TO true

print ("lunch", "bfast" in ['lunch','bfast','dinner']) ## lunch True

a = "lunch", "bfast" in ['lunch','bfast','dinner']
print (a)

print(meals[:3])

meals = ['lunch','bfast','dinner','supper','tiffin','coffee']
print (meals[1:])
print (meals[0:]) ## all elements are printed
print (meals[:]) ## all elements are printed...
print (meals[2:])
print (meals[1:-1]) ## -1 element not included...
print (meals[-4:-2])
print (meals[::]) ## all elements are printed...
print (meals[::1]) ## all elements are printed...
print (meals[::2]) ## print from start, hop by 2...
print (meals[::-2]) ## print from last, hop by -2...


actors = ["Schwarzenegger", 
          "Seagal", 
          "Lundgren", 
          "Stallone", 
          "Snipes", 
          "Van Damme", 
          "Willis", 
          "Norris", 
          "Li", 
          "Statham", 
          "Chan"]
print(actors[:-5])
print(actors[-3:])

i = 0

while i <= 5:
    print (i)
    i += 1
else:
    print ("hello") ## this will anyway be printed...


actors = ["Schwarzenegger", 
          "Seagal", 
          "Lundgren", 
          "Stallone", 
          "Snipes", 
          "Van Damme", 
          "Willis", 
          "Norris", 
          "Li", 
          "Statham", 
          "Chan"]

#print(reversed(actors))

#for idx, actor in enumerate(actors):
#    print (idx + 1, actor)

for a in actors[::-1]:
    print (a)

for index, num in enumerate([1, 1, 2, 2, 5]):
  if index > num:
    break
  print(num)

print ("\"Hello\"") 
print ("'Hello'") 

file_name = r"c:\news\file"
print(file_name)

print(dir([]))

print("pasta".__len__())

print (format(123421322,","))

print (max(["A", "a", "Z", "z"]))

numbers  = [3,6,7,8,9]
cubes = [number **3 for number in numbers ] ## list comprehension...
print(cubes)

print(all("A","a"))

print ([1,2] * 3)