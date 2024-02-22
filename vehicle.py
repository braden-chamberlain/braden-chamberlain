# imagine i want to list these vehincles on craigslist
class Vehicle:


    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        return 'HOOOOOOONK!'

    def drive(self, miles_driven):
        self.mileage += miles_driven
        return self.mileage
    
    def __repr__(self):
        return f'A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles. {self.honk()}'
    
# if __name__ == '__main__':
    # my_vehicle = Vehicle('Hyundai', 'Ioniq5', 'Teal', 2022, 25000)

    # print(my_vehicle)


# this is called the child calss because it inherited things
#from the parent class
#convertible class inherits from vehicle
class Convertible(Vehicle):

    def __init__(self, make, model, color, year, mileage, top_down=True):
        #super init replaces all the other lines
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down

#these get carried over
    # def honk(self):
    #     return 'HOOOOOOONK!'

    # def drive(self, miles_driven):
    #     self.mileage += miles_driven
    #     return self.mileage
#because this is inside the helper class, it applies only to this   
        
    def change_top_status(self):
        if self.top_down:
            self.top_down = False
            return "top is now up"
        else:
            self.top_down = True
            return 'top is now down'
    
    def __repr__(self):
        return f'A {self.color} {self.year} {self.make} {self.model} convertible with {self.mileage} miles. {self.honk()}'
    
if __name__ == '__main__':
    my_vehicle = Convertible('Hyundai', 'Ioniq5', 'Teal', 2022, 25000, top_down=False)

    print(my_vehicle)
    print(my_vehicle.top_down)
    my_vehicle.change_top_status
    print(my_vehicle.top_down)
