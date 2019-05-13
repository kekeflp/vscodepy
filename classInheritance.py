# __*__ coding=utf-8 __*__


class Car():
    def __init__(self, make, year, model):
        self.make = make
        self.year = year
        self.model = model
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("这车已经使用 " + str(self.odometer_reading) + " 公里了.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你无法回调里程表!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas(self):
        print("我有一个大油箱！")


class ElectricCar(Car):
    # 定义子类，继承调用父类（super()）的构造函数
    def __init__(self, make, year, model):
        super().__init__(make, year, model)
        # 将实例当成属性使用，就可以调用此实例内部的方法了
        self.battery = Battery()

    def trans_tank(self):
        print("我会变成坦克.")

    # 子类重写父类方法，直接定义个与父类相同的方法
    def fill_gas(self):
        print("我是电动车，不需要油箱")

#   def describe_battery(self):
#        print("这车拥有 " + str(self.battery_size) + "-kwh 的电量.")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("这车拥有 " + str(self.battery_size) + "-kwh 的电量.")

    #定义对应电量形式的里程数
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        msg = "这车满负荷可以行驶 " + str(range)
        msg += " 公里。"
        print(msg)


my_car = ElectricCar("tesla", 2016, "model s")
#子类调用父类的方法
print(my_car.get_descriptive_name())
#子类调用子类的方法
my_car.trans_tank()
father_car = Car("bwm", 2017, "s520")
#父类调用的自己的方法
father_car.fill_gas()
#子类调用的是自己的方法，相当于重写了父类
my_car.fill_gas()
#子类的属性调用其他类实例
my_car.battery.describe_battery()
my_car.battery.get_range()
