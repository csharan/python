x = 123
     
def sum_of_digits(y):
    sum = 0
    while (y != 0):
        sum = sum + int(y % 10)
        y = int(y / 10)
    print(sum)
     
sum_of_digits(x)


list = ['p', 'q', 'r']
 
def func(char):
   char.pop()
   char.append('s')
   print(char)
 
func(list)
print(list)


'''
There are 4 members
in my family
'''
print("I love coding")

#for 'o' in "Books":
 #   print(ch,end=" ")

print (11/3)
print (11//3)