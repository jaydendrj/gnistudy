'''一个可以用于表示汽车的类'''
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+' '+self.model
        return long_name

    def read_odometer(self):
        print('This car has '+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self,mileage):
        if mileage<self.odometer_reading:
            print('You can\'t roll back an odometer!')
        else:
            self.odometer_reading=mileage

    def increment_odometer(self,miles):
        if miles<0:
            print('You can\'t roll back an odometer!')
        else:
            self.odometer_reading+=miles


class Battery():
    def __init__(self, battery_siz=70):
        self.battery_size = battery_siz

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-Kwh battery.")

class ElectricCar(Car):
        def __init__(self, make, model, year):
            super().__init__(make, model, year)
            self.battery=Battery()

        def fill_gas_tank(self):
            print('This car doesn\'t need a gas tank!')


def f(x):
    return -x