def simple_chart(a):
    for i in range (a):
        print ("rr" * i)
    #i = 0
    ##return a

xx = simple_chart(5)
print("value of xx is :", xx)

def fun_learn (a, c=100, b=200):
    print(a,b,c)

fun_learn (100, b= 2, c= 3)
fun_learn (100, 200, 300)
fun_learn (100, c= 2, b= 3)

for i in range (1,5):
    for j in range (1,5):
        print (i,j)
        if i == 3:
            break ## breaks only inner loop


def fun(x,y):
    if x == y:
        return x
    else:
        return fun (x, y-1)
    #print (x,y)

##print (fun(0,3))

fun(0,3)


def func():
    global var
    print (var)
    var = "hello2"

var = "hello" ## can be acceesed within the function
func()
print(var)

##########################################################################################


def func():
    ##var = var + 300 ## wil cause error...
    return var - 100

var = 100 ## can be acceesed within the function
var2 = func()
print(var2)

def func():
    ##var = var + 300 ## wil cause error...
    return var - 100
##########################################################################################
var = 100 ## can be acceesed within the function
var2 = func()
print(var2)

print (1 + 2*3//4)
##########################################################################################
## function can return multiple values...
def func(a,b):
    return a,b
f, c = func(1,2)
r = func(100,200)[0] ## only one return varianble can be accessed like this...
print(f,c,r)
##########################################################################################