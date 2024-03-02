import sys

print(sys.argv)

def total_marks(mark_list):
    return(sum(mark_list))
    
def pass_or_fail():
    if total_marks() > 100:
        result = "PASS"
    else :
        result = "FAIL"
    return result

pass_or_fail([100,100])

print ("hello".__dict__.keys())

for pname in 'hello'.__dict__.keys():
    print (pname)