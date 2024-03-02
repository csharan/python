a = [1,2,3,4,5,6,7,8]
b = [6,7,8,9]
c = a + b ## this only does concatenation
print (c)
a.sort # sorts the list, list order gets changed...
print (a)

d = a * 3 ## this creates a new list, does not actually multiply..
print (d)

#e = b + 7 ## does not work
#d = a * b ## does not work

a = [1,2,3,4,5,6,7,8]
print ("pinting reversal a:", a[::-1]) ## reverses the list...
print ("pinting reversal a:", a[-1::]) ## only last digit is shown...
print ("pinting reversal a:", a[-3:-1]) #last digit is not shown...

a = [1,2,3,4,5,6,7,8]
print ("pinting a:", a[:]) #prints complete list
print ("pinting a:", a[::]) #prints complete list
print ("pinting a:", a[::1]) ## prints complete list as it considers 1 as skip element

print ("pinting a:", a[::2]) 
print ("pinting a:", a[1:]) ## from index 1 item to last

def fruit(chart):
    return ["Apple","Kiwi"]
cart = ["Orange","Mango","Banana","Grapes"]
new_cart = fruit(cart)
print(new_cart)

print ([1,2] + 3)

## learning point...
action_stars = ['arnold','willis','stallone','tom']
#second_stars = action_stars.pop(1)
#print(second_stars)
print (action_stars.reverse())

# remove (by value), del (delete one or more items with index), pop (by index), clear...
# reverse (returns none, mutates), sort (mutates), extend, enumurate,
#append (adds to last), extend, insert (by index)
#conversion functions - list, tuple, dict, str, int.....

action_stars = ['arnold','willis','stallone','tom']
action_stars.append("hanks")
action_stars.append(["hanks","robin"])
print(action_stars)
a = action_stars.append(["hanks","robin"])
print(a)

action_stars = ['arnold','willis','stallone','tom']
action_stars.extend ("Kamal") 
action_stars.extend (["Kamal"]) 
print(action_stars)

action_stars = tuple(['arnold','willis','stallone','tom'])
print(type(action_stars))

action_stars = ['arnold','willis','stallone','tom']
action_stars = ('arnold','willis','stallone','tom')



for i in action_stars:
    print (i)

## list comprehension...
action_stars = ['arnold','willis','stallone','tom']
action_stars_2 = [i for i in action_stars if i != "tom"]
print (action_stars_2)

## tuple.. comprehension...
action_stars = ('arnold','willis','stallone','tom')
action_stars_2 = tuple([i for i in action_stars if i != "tom"])
print (action_stars_2)

ranges = [i for i in range(0,5)]
print (ranges)

data = ""
while data:
   print("Data is not Empty")
else:
   print("Data is Empty")

t = ("sandy", "mandy", "candy","andy")
print(sorted(t))
print(sorted(tuple(t)))

print(dir(list))

t = ("sandy", "mandy", "candy","andy")
#t[1][1] = "R"
print(t[1][1])

t = ("sandy", "mandy", "candy","andy")
name1, name2, name3, name4 = t
print (name1, name2, name3, name4)

t = ("sandy", "mandy", "candy","andy")
r = ("sandy", "mandy", "candy","andy")
name1, name2, *names = t
*names, name1, name2 = r
name1, *names, name2 = r
name1, name2, name3, *name4 = r
print(name1, name2, names, sep = ",")

def arg_sample (*args):
    print(args)

arg_sample (1,2,3,4,5)


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
#
# Write your code here.
#
print("The list with unique elements only:")
print(my_list)

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)

for i in range(-1,1):
    print (i)

my_list = [0 for i in range (1,3)]
print(my_list)

my_list = [1 for i in range (1,3)]
print(my_list)

a = [1,2,3,4,5,6]

del a[2]

print (a)

a[2] = 100

print(a)

my_list = ['mary','had','a','little','lamb']
def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'
print(my_list)

t = ["sandy", "mandy", "candy","andy"]
t.index(0)

tup = (1,2,4,8)
tup = tup[-2:-1]
print(tup)
tup = tup[-1]
print (tup)

my_list = [1,2]
for v in range (2):
    print(my_list[v])
    my_list.insert(-1,my_list[v])
print(my_list)

[1,2,1,2]

angle = 1
for i in range (2,5):
    if 2 * i > 4:
        angle += 1
else:
    angle -= 1

print(angle)

print(1+1//2*3)

power = 1
while power < 5:
    power += 1
    print ("@", end = "")
    if power == 3:
        break
else:
    print("@")

list_one = [1,2]
list_two = list_one
list_two.append(3)
print(list_one[-1])


b = a[2:5]
print(b)

a = [1,2,3]
print (a.index(1))
print (a[:2])

print (a[])

a = [1,2,3,4,5]
print (a[3:10]) ## does not produce error...
print(a[6]) ## produces error

action_stars = ['arnold','willis','stallone','tom']
#action_stars.pop() ## deletes last item
#action_stars.pop(-2) ## deletes item by index
print(action_stars)

action_stars = ['arnold','willis','stallone','tom']
#action_stars[1] = "kamal" ## does a replace...
action_stars.insert(1, "kamal") ## moves the item...
print(action_stars)

power = 4

power *= 2
print(power)

angle = 1
for i in range (2,5):
    if 2 * i > 4:
        angle += 1
else:
    angle -= 1

print(angle)

print (4 - 3 // 2 + 1)

tup = (1,"d",5)

def walk(top):
    if top == 0:
        return 0
    return top + walk(top-1)

print(walk(2))

answers = (True, False, True)
print(answers[-1:])

power = 2

while power < 5:
    power += 1
    if power == 3:
        continue
    print("@", end = '')
else:
    print ("@")

others = 1
for i in range (2,4):
    for j in range (-1,2):
        if  i == j:
            other += 1
        else:
            break
print (others)

print (0//2)

torque = 0
while torque != 0:
    torque //= 2
    print("*", end)
else:
    print("*****")
            
print(1+2*3//4)

angle = -1
for i in range(-1,1):
    if 2 * 1 < 4:
        angle += 1
else:
    angle += 2
print(angle)

train_speed = {1 : 2, 56:78, 777:988}
for train in train_speed.items():
    print(train, end = "")

a = [111,222,3333]
print(a.index(222))

def sample(value):
    return total - value

total = 4
total = sample(2)
total = sample(1)
print(total)

l = ['a', 'b', 'c', 'd', 'e','f']
print(l[1:])
print(l[-2:])
print(l[-1:])
print(l[:-2])
print(l[-4:-2])

l1 = ['True','True','False','True','Hello']
for i in l1:
    if i:
        print ("Hello")

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 +  l2 
print(l3[0])
print(type(l3))

l1 = (1,2,3)
l2 = (4,5,6)
l3 = l1 +  l2
print(l3[0])
print(type(l3))

print (4.0//3)