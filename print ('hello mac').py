#print ('hello mac')

#def printf(a):
#    print (a)

#printf('hey this is from a function')

#for i in range(0,5):
#    print (i, end = '-')

def sum_of_list(listvar):
    j = 0
    k = len(listvar)
    for i in listvar:
        j = i + j
        #print(j)
    #print(j)
    #return j
    return j / k

a = sum_of_list([5,6,7,8])

print ('sum of given list is ', a)

