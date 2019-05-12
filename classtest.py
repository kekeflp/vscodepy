# __*__ coding=utf-8 __*__


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 50

    def get_descriptive(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        #②self.odometer_reading = mileage
        '''
        ③将里程表设置为指定值
        禁止将里程表读数往回调
        '''
        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

'''
new_car = Car("audi", "a4", 2016)
print(new_car.get_descriptive())
#①new_car.odometer_reading = 23
#②new_car.update_odometer(10)
#③new_car.update_odometer(10)
new_car.read_odometer()
'''
my_car = Car("subaru", "outback", 2013)
print(my_car.get_descriptive())
my_car.update_odometer(100)
my_car.read_odometer()
my_car.increment(20)
my_car.read_odometer()

'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+"is now sitting.")

    def roll_over(self):
        print(self.name.title()+"rolled over!")


my_dog = Dog("willie ", 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()
'''

'''
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This is my favourite " + self.restaurant_name + ".")

    def open_restaurant(self):
        print(self.cuisine_type + " is opening!")


my_restaurant = Restaurant("old man", "chinese")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
'''
