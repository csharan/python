thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict['model'])

thisdict = dict(name = "John", age = 36, country = "Norway") ##dict constructor
print(thisdict)
##update
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

##add
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
##remove
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

##print keys of a dict
for x in thisdict:
  print(x)

for x in thisdict.keys():
  print(x)

##print values of a dict
for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)

dict1 = {'one': 1, 'two': 2, 'three': 3}
dict2 = {'one': 1, 'two': 5, 'four': 8}
dict3 = dict(dict1)
dict4 = dict(dict2)
dict3.update(dict2)
dict4.update(dict1)
print(dict3 == dict4)



    temp = [[3 - i for i in range(2)] for j in range(3)] 
    print(temp)

    x = 4
    y = 5
    z = 3
    print(x == y or z)

    def myfun(x):
            if x == 0:
                    return 1
            return x + myfun(x-1)
      
    print(myfun(5))

    def boo(x):
            if x == 1:
                    return x
            return x * boo(x-1)
     
    print(boo(3))


    x = [
        'a',
        'b',
        {
            'one': 1,
            'two':
            {
                'x' : 10,
                'y' : 20,
                'z' : 30
            },
            'three': 3
        },
        'c',
        'd'
    ]
    print(30 in x[2])

    d1 = {"sandy":35, "surname":"Kate"}
    d2 = {"surname":"Kate", "sandy":35}
    print(d1 == d2)

def f1(num):
    if num %2 == 0:
        return True
    else:
        return False
     
x = f1(2)
print(not x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print (len(thisdict))

for i in thisdict:
    print (i)


## accessing dict using key...
print(thisdict["brand"])
## accessing dict using get method...
print(thisdict.get(("brands"),["hello"]))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["version"] = ("battery")

thisdict.setdefault("color","red") ## add this pair if its not present...

print (thisdict)

###############################################################################
movies = { 
    "horror" : ["ex","sc","scream"],
    "action" : ["die", "casi", "gone"],
    "comedy" : ["fire","true","liar"] 
    }

#print(movies["horror"]["sc"]) ## does not work
#print(movies["horror"][1]) ## does not work
i = 0
for m in movies:
    i = i + 1
    print(m, ":", movies[m])

###############################################################################

movies = { 
    "horror" : ["ex","sc","scream"],
    "action" : ["die", "casi", "gone"],
    "comedy" : ["fire","true","liar"] 
    }

for key, value in movies.items() :
    print (key, ":", value)

movies = { 
    "horror" : ["ex","sc","scream"],
    "action" : ["die", "casi", "gone"],
    "comedy" : ["fire","true","liar"] 
    }

for _, value in movies.items() : #_ ignores the key in this case...
    print (value)

print(sorted(movies))

movies = { 
    "horror" : ["ex","sc","scream"],
    "action" : ["die", "casi", "gone"],
    "comedy" : ["fire","true","liar"] 
    }

for k in movies.keys() :
    for v in movies.values():
        print (k,v)

for m in movies.values() :
    print (m)

print(dir(dict))

##clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

######################################################################
def my_func(a, b, *args, **kwargs):
  print(a,b, sep = ",")
  print(args) ## gives tuples...
  print(kwargs) @@ gives dictionaries...

my_func( 20, 30, 40,50, x = 9, y = 100)
######################################################################



print(dir(dict))

['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


print(1//2*3)

y = 2 + 3 * 5.

print (1/1)

print (4/5)

print (2//4)

print ( "vlue is ", 4%2)
print ( "vlue is ", 2%4)

sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

nums = []
vals = nums[:]
vals.append(1)
print(vals, nums)



for i in range(1):
    print (i)

var = 1
while var < 10:
    print("#")
    var = var << 1

print (var)


def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))


def fun (intl =2, out = 3):
    return intl * out

print(fun(3))

def fun(x):
    global y
    y = x * x
    return y

fun (2)
print(y)

def fun (x,y,z):
    return x +2 * y + 3 * z

print(fun(0, z=1, y = 3))

tup = (1,2,4,8)
tup = tup[1:-1]
tup = tup[0]
print (tup)

def func(a,b):
    return a * a

print(func(2))

my_list = ['Mary','had','a','little','lamb']

def my_list(my_list):
    del my_list[3]
    my_list [3] = 'ram'

print(my_list(my_list))

tup = (1,2,3,4,5,6)
print(tup)
tup = tup[1:4]
print(tup) ## tuples can be sliced
print(type(tup))

var = 1
#var = var << 1
#print(var)
var2 = var >> 1
print(var2)

print (3%4)

a = 5
b = 6

c = a ^ b

print (c)

a = input("hello")
print(a)

a = b = 5

a = 5 = b

print (a,b)

a = 5
c= 10
b = 4
print (a < b and a < c or a < c )

a = None 

print(a)

###################################################
my_list = [1,2,3]
for v in range (len(my_list)):
    #print(v)
    my_list.insert (1,my_list[v])
    print(my_list[v])
#print(my_list)
###################################################
    
my_list = [1,2,3]
#print(len(my_list))
for v in range (len(my_list)):
    my_list.insert (1,my_list[v])
    #print(my_list[v])
print(my_list)

###################################################
    
tup = (1,) + (1,)
print(tup)
tup = tup + tup
print(tup)
print(len(tup))

tup = [1,3] + [1,5]
tup = tup + tup
print(tup)

tup = [1,3] + [1,5]
tup = tup * tup ## does not work...
print(tup)

tup = [1,3] * 2
print(tup)





## Ways of accessing dictioanry items...
thisdict = {
  "brand": ["Ford","toyota","honda"],
  "model": "Mustang",
  "year": 1964
}

for i in thisdict: ## prints only keys...
    print (i)

for i , j in thisdict.items():
    print (i,j)

for i in thisdict.keys():
    print (i)

for i in thisdict.values():
    print (i)

##########################delete##############################################

thisdict = {
  "brand": ["Ford","toyota","honda"],
  "model": "Mustang",
  "year": 1964
}    

##thisdict.popitem() ## removes last item...
thisdict.pop("brand") ##removes the item based on key value

print(thisdict)
########################################################################

thisdict = {
  "brand": ["Ford","toyota","honda"],
  "model": "Mustang",
  "year": 1964
}    
thisdict["color"] = ["Red","blue","white","orange"] ## adds the key value pair
print(thisdict)
thisdict["color"] = ["black","blue","white","violet"] ## updates the value if key already exists
print(thisdict)
thisdict = dict()
print(thisdict)
thisdict["color"] = ["Red","blue","white","orange"]
print(thisdict)
########################################################################

thisdict = { "brand": ["Ford","toyota","honda"], "model": "Mustang", "year": 1964}
newdict = {"color" : ["red","white","blue"]}
thisdict.update(newdict) ## adds the new key
print(thisdict)
newdict1 = {"color" : ["black","orange","violet"]} # updates the key
thisdict.update(newdict1)
print(thisdict)
########################################################################
thisdict = { "brand": ["Ford","toyota","honda"], "model": "Mustang", "year": 1964}
print(thisdict["brand"])
for d in thisdict:
    print (thisdict[d]) ## prints values
for d in thisdict:
    print (d) ## prints keys
########################################################################
thisdict = { "brand": ["Ford","toyota","honda"], "model": "Mustang", "year": 1964}
thisdict1 = sorted(thisdict)
print(thisdict1)
########################################################################

def cdict(**kwargs):
    return(kwargs)

newdict = cdict(a = 10, b = 20, c =30)

print(newdict)
########################################################################

def cdict(a,b,c,*args,**kwargs):
    print(args)
    print(kwargs)

cdict(10, 20, 30, 60, 70, 80, 90, 100, 200, k = 300)
########################################################################

dictionary = {}
my_list  = ['a','b','c','d']

for i in range (len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i],)

print(dictionary)

my_list  = ['a','b','c','d']
print(len(my_list))
for i in range (len(my_list)):
    print(i)

var = 0
while var < 6:
    var += 1
    if var %2 == 0:
        continue
    print("#")

for i in range(1,-1):
    print(i)

x = lambda a : a + 10
print(x(5))

dictionary = {'one':'two','three': 'one','two':'three'}
v  =dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

print(v)
a = None
if a == None:
    print("hello")

print(None + 1)

dct = {'one':'two','three': 'one','two':'three'}
v = dct['three']
print (dct['four'])
print(v)
#print(len(dct))
d = dct[v]
print (d)

for k in range (len(dct)):
    v = dct[v]

print(v)

dct = {'one':['two','nine'],'three': 'one','two':'three'}
print (dct["three"])
print(dct)

dct = {'one':['two','nine'],'three': 'one','two':'three'}
print (dct["one"][0])

dct = {'one':'two','three': 'one','two':'three'}
print (dct["one"][2])

dict = {'one':'two','three': 'one','two':'three'}

for v,k in dict.items():
    print (v[0])

dict = {'one':'two','three': 'one','two':'three'}

for v in dict.items():
    print (v[0])

dict = {'one':'two','three': 'one','two':'three'}

#for v,k in dict.items():
#    print (v[0])

dict['three'] = 'fivehundrd'

print(dict['three'])