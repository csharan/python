class Cars():
    def __init__ (self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self.price = 100000

carlist = [["Red","Honda","2021"], ["Blue","Toyota","2021"], ["White","Honda","2021"]]

for allcars in carlist :
    mycar = Cars(allcars[0], allcars[1], allcars[2])
    print (mycar.color, mycar.model, mycar.year, mycar.price)

