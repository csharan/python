import math as m
#for name in dir(m):
#    print (name, end = "\t")
#print(m.floor(-5.0))

import random as r
#r.seed(0)
#print(r.random())
#li = ['saravana','sharan','ananthan','ajit','priyank']
#print(r.sample(li,5)) ## prints randomly...
#print(r.sample(li,6)) ## errors out...
#print(r.choice(li)) ## prints randomly...
#li2 = [['saravana','sharan','ananthan','ajit','priyank'],['hello','boss']]
#print(r.sample(li2,1)) ## prints randomly...
#print(r.sample(['saravana','sharan','ananthan','ajit','saravana'],2)) ## prints randomly...
## above one can return - ['saravana', 'saravana'] as well...

import platform as p 
print(p.platform())
print(p.platform(True, True))
print(p.machine())
print(p.processor())
print(p.system())
print(p.python_implementation())
print(p.python_version_tuple()) # ('3', '11', '8')
print(p.version())

import random
def generate_tickets(ticket_count, max_number):
    list_to_return = random.sample(range(0, max_number), ticket_count)
    return (list_to_return, random.sample(list_to_return, 1)[0])

a = generate_tickets(30,58)
print (a)
