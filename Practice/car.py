class car():

    def __init__(Self, model, colour, initial_speed = 0):
        Self.model = model
        Self.colour = colour
        if initial_speed < 0:
            Self.__speed = 0
        else:
            Self.__speed = initial_speed

    def speed_up (Self):
        Self.__speed += 5
    
    def slow_down(Self):
        if Self.__speed < 5:
            Self.__speed = 0
        else:
            Self.__speed -= 5
    
    def show_speed(Self):
        print("current_speed is: ", Self.__speed)

my_car = car("Maruti","red", 50)
my_car.speed = -100
my_car.show_speed()