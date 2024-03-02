"""test code
all are comments"""
print ("you a're right") # using single quotes in a string
print ('you a"re right') # using dounble quotes in a string

print ( 3 + 5 - 10 // 2 + 6)

# print ("hello", "world", sep = "$", end = "^") 
# print ("hello", "world", "python", sep = "$", end = "#") 

# print (end = "$", "hello", "world", "python", sep = "#") ## will not work

# print ("hello", sep = "$", end = "^")

print (6/3)
print (14 // 3)
print (-14//3) ## see the difference...
print (-14//-3) ## see the difference...floor division
print (14//-3) ## see the difference...
print(1%3)
print(2%3)

print(5 <> 5)

print (3.0 == 3)

print(type(True))

print ("Hello" + 5) ## does not work
print ("Hello" + str(5)) ## does  work
print ("Hello" * 5) 
##########################################################
strings = "{} hello {}"
print(strings.format("GM","HRU"))

strings = "{name} hello {greeting}"
print(strings.format(greeting = "HRU", name = "Sharan"))

##########################################################
name = "sharan"
strings = f"{name} , hello world"
print(strings.find("s")) ## returns -1 when value not found, program continues...
print(strings.index("s")) ## returns error when value not found, program aborts..
print(name[1]) ## string index start at 0...
print(strings.count("sh"))
print(strings.count("s") + strings.count("h") )
print(strings.startswith("s"))
print(strings.endswith("s"))
strings = "sharan hello Hru DOING"
print(strings.title())
print(strings.capitalize())
print(strings.lower())
print(strings.upper())
print(strings.swapcase())
print(strings.lstrip())
print(strings.rstrip())
print(strings.strip("shG"))
print(strings.replace("h","p"))
##########################################################
playwright = "Shakespeare"
print(playwright[0])

print("geronimo"[0:9:2])
print("genuflect"[::-1])
print("mastodon"[-5::2])