class objarea:

    def __init__(self,diagname,diagtype = "2dimensional"): ## this is called the constructor...
        self.diagram_name = diagname
        self.diagram_type = diagtype
        self.ismathematical = True ## defaulted...

    def area(self,length,breadth):   
        return length * breadth

    def cube(self,length,breadth,width = 10):   
        return (length * breadth * width) , (length * breadth) ## returns 2 values...
## class definition ends here..
        
areaa = objarea('square') # whenever an object is created, it has to be called with the attributes...
cubea = objarea('cube','3dimensional')

#areaa.diagram_name = 'modified square'

print("area of given:" , areaa.diagram_name ,"is", areaa.area(10,10), "its a ", areaa.diagram_type,
       "shape", areaa.ismathematical)
print("cube of given:" , cubea.diagram_name ,"is", areaa.cube(10,10,20)[0] , "its a ", cubea.diagram_type , 
      "shape")