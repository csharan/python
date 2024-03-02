## sample program that shows example of using a class...

class mychart:
    def __init__(self, cname, ctype): ## only one init method can be implemented
        self.cname1 = cname
        self.ctype1 = ctype

    def simple_chart(self,a):
        print("@" * a)
    
    def tree_chart(self,a,b = 20):
        print("%" * a)    
        print("^" * b)

chart1 = mychart("hist_sample", "histogram") ## when ever you create an object pass the attributes
chart2 = mychart("poly_sample", "polygram")

chart1.simple_chart (10)
chart2.tree_chart (b=10,a=100)## this works

print(chart1.cname1 + " "+ chart1.ctype1)
print(chart2.cname1)