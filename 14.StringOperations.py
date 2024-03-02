print('helloworldsharan'[0]) ## string index...
print (2 * 'hello')
print ('hello' * 2)
print ('hello' + 'hello')
print('helloworldsharan'.index('p')) ## if string is not found, error is raised...
print('helloworldsharan'.index('lo'))
print('helloworldsharan'.find('sh'))
###
print('helloworldsharan'.find('p')) ## if string is not found, -1 is printed...
print('helloworldsharan'.find('h',4)) ## if string is not found, -1 is printed...
print('helloworldsharan'.find('h',4,8)) ## if string is not found, -1 is printed...

print('helloworldsharan'.rfind('h')) ## searches from right...
print('helloworldsharan'.rfind('h',4)) ## if string is not found, -1 is printed...
print('helloworldsharan'.rfind('h',4,8)) ## if string is not found, -1 is printed...

a = 'helloworldsharan7'
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.islower())
print(a.isupper())
print(a.isspace())


print('@@'.join(['hello','sharan','world']))
print('@@'.join(['hello','sharan','world']))

a = 'hello world shar\nan7'
print(a.split())

names = ['arjun','jia','nethra']
names2 = sorted(names)
names23 = names.sort()
print(names)
print(names2)
print(names23)

print(ord('d') - ord('a'))

print(len('\'\\') - len('\n'))

print('work work work'.rfind('work', 0, 5))

print('30' > '7')
print('30' > 7)

print('John'.isalnum())
print('John1990'.isalnum())
print('John 1990'.isalnum())
print('John-1990'.isalnum())
print('John_1990'.isalnum())