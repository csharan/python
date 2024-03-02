def fun_add (a,b):
    return a + b
x = fun_add(5,10)
print(x)

x = lambda a,b :  a + b ## can be assigned to a variable...
print (x(5,10))
###################################################################################
numbers =[1, 2, 3, 4, 5]
sq = []

for a in numbers:
    a *= a
    #print(sq)
    sq.append(a)
print(sq)

## same functionality using lambda..
squared_numbers = map(lambda x: x * x, numbers)  # Apply lambda function to each element in numbers
print(list(squared_numbers))
##################################################################################
class Vehicle:
  def __init__(self, speed):
    self.speed = speed + 5
 
car = Vehicle(10)
print(car.speed)

class Void:
  pass
 
first_num = 5
second_num = 5
first_obj = Void()
second_obj = Void()
print(first_num is second_num and first_obj is second_obj)

class Animal():
    def produce_sound(self):
        print('General animal sound')
 
class Dog(Animal):
   pass
#    def produce_sound(self):
#        print('woof, woof!')
 
class Labrador(Dog):
   pass
#   def produce_sound(self):
#      print('labrador woof!')
 
my_pet = Labrador()
my_pet.produce_sound()

