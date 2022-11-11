"""vehicle module"""
import datetime




class Vehicle:
    """vehicle class """
    def __init__(self, name, reg_no, manufacturer, mileage, capacity, length, width):
        self.v_name = name
        self.v_reg_no = reg_no
        self.v_manufacturer = manufacturer
        self.v_mileage = mileage
        self.v_capacity = capacity
        self.v_width = width
        self.v_length = length

    def exit_time(self):
        out_time = datetime.datetime.now()

    def entry_time(self):
        self.intime = datetime.datetime.now()


class Car(Vehicle):
    """Car class that inherits the property of Vehicle class"""
    def __init__(self, name, reg_no, mileage, capacity, manufacturer, length, width):
        super().__init__(name, reg_no, mileage, capacity, manufacturer, length, width)


class Bike(Vehicle):
    """Bike class that inherits the property of Vehicle class"""
    def __init__(self, name, reg_no, mileage, capacity, manufacturer, length, width):
        super().__init__(name, reg_no, mileage, capacity, manufacturer, length, width)


class Bus(Vehicle):
    """Bus class that inderits the property of Vehicle class"""
    def __init__(self, name, reg_no, mileage, capacity, manufacturer, length, width):
        super().__init__(name, reg_no, mileage, capacity, manufacturer, length, width)

