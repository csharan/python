#print(val)
try:
    a = [1,2,3,4,5]
    val = len(a) ## will give an integer..
    #val = int("aa")
    #val = "0"
    print(val/val)
except NameError:
    print("Name error - Name not defined")
#except BaseException:
#    print("BaseException ")
except ZeroDivisionError:
    print("zero division error")
except ValueError:
    print("Val error")
except TypeError:
    print("TypeError")
except:
    print("some error")
#finally: 
#    print("all good")   
######################################################################################################
def divide_by (n):
    try:
        a = 5 / n
    except:
        a = 10 ## returns a default value if there is an error...
    return a
######################################################################################################
print(divide_by("a"))
# raise exceptions :
def add_numbers(a,b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError("entered negative numbers")
        return a + b       
    except ValueError as e:
        return f"caught error : {e}"
    else:
        print(" else will be raised when there is no exception")

print(add_numbers(2,5))

## raise user defined exceptions
## it should be defined in a class...
class raiseerr(Exception):
    pass

def add_numbers(a,b):
    try:
        if a <= 0 or b <= 0:
            raise raiseerr("entered negative numbers")
        return a + b       
    except raiseerr as e:
        return f"caught error : {e}"
    else:
        print(" else will be raised when there is no exception")

print(add_numbers(2,5))

AttributeError
SyntaxError
TypeError
ValueError


strng = "File"
print(strng)
strng = "File" + "File"
print(strng)

a = [1,2,3]
b = sum(a)
print(b)

def fun (inte=2, out=3):
    return inte * out

print(fun(3))

print(1%2)

0,1,9,16

lst = [i for i in range(-1,-2)]
lst = [1,2,3]
print(lst)
lst.index(0)

try:
    print(5/0)
    break
except:
    print("error man")
except (ValueError, ZeroDivisionError):
    print("too bad")

print(1/5)

[0,1,2] [0,1,2]


foo = (1,2,3)
print(foo.index(0))

a= 0
print(len(a))

try:
    value = "0"
    print(int(value)/len(value))
except ValueError:
    print ("value error")
except ZeroDivisionError:
    print("Zero error")
except TypeError:
    print("type error")
except:
    print("Boo!!")


l = [0]

print(l[1])

tup  = (1,2,4,8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

print(dir(tuple))