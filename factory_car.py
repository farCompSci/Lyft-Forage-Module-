import datetime
from abc import ABC, abstractmethod, abstractproperty
from datetime import date


# TODO 1: Making the Engine Interface
class Engine(ABC):
    """Engines Interface for implementation"""

    @abstractmethod
    def need_service(self) -> bool:
        """Checks if the car needs service"""


# TODO 2: Making the Engine implementations
class CapuletEngine(Engine):
    """Capulet Engine is implementation of the Engine Abstract Class"""

    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.last_service_mileage = last_service_mileage  # some int representing the number of miles since last service
        self.current_mileage = current_mileage  # the mileage at which the car currently is at.

    def need_service(self) -> bool:
        """Checks if mileage is greater than miles necessary for service, in this case 30_000"""
        if (self.current_mileage - self.last_service_mileage) > 30_000:
            return True
        return False


class WilloughbyEngine(Engine):
    """Willoughby Engine is implementation of the Engine Abstract Class"""

    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def need_service(self) -> bool:
        """Checks if mileage is greater than miles necessary for service, in this case 60_000"""
        if (self.current_mileage - self.last_service_mileage) >= 60_000:
            return True
        return False


class SternmanEngine(Engine):
    """Sternman Engine is implementation of the Engine Abstract Class"""

    def __init__(self,warning_indicator_status: bool):
        self.warning_indicator_status = warning_indicator_status  # In this case warning indicator status determines whether servicing is necessary

    def need_service(self) -> bool:
        """Checks if services are necessary, which happens only if warning indicator is on / denoted by True"""
        if self.warning_indicator_status:
            return True
        else:
            return False


# TODO 3: Making the Battery Interface
class Battery(ABC):
    """Battery Interface for implementation"""

    @abstractmethod
    def need_service(self) -> bool:
        """Checks if the battery needs service"""


# TODO 4: Making Battery Implementations
class SpindlerBattery(Battery):
    """Spindler Battery is an implementation of the Battery implementation"""

    def __init__(self, current_date: int, last_service_date: int):
        self.current_date = current_date  # Getting current date in years
        self.last_service_date = last_service_date  # Getting the year of Battery's last service

    def need_service(self) -> bool:
        """Battery needs service if it has not been serviced in 3 years"""
        if (self.current_date - self.last_service_date) >= 3:
            return True
        return False


class NubbinBattery(Battery):
    """Spindler Battery is an implementation of the Battery implementation"""

    def __init__(self, current_date: int, last_service_date: int):
        self.current_date = current_date  # Getting current date in years
        self.last_service_date = last_service_date  # Getting the year of Battery's last service

    def need_service(self) -> bool:
        """Battery needs service if it has not been serviced in 4 years"""
        if (self.current_date - self.last_service_date) >= 4:
            return True
        return False

#TODO 5: Making the new Tires Interface
class Tires(ABC):
    """Adding Tires Interface"""

    @abstractmethod
    def need_service(self) -> bool:
        """Checking the tires to see if any needs service"""

#TODO 6: Making the Tires Implementations
class CarriganTires(Tires):
    def __init__(self,tires_state):
        self.tires_state = tires_state # Getting the state of the tires in an array

    def need_service(self) -> bool:
        """Checking the tires array"""
        for tire in self.tires_state:
            if tire >= 0.9:
                return True
        return False

class OctoprimeTires(Tires):
    def __init__(self,tires_state):
        self.tires_state = tires_state #Getting state of the tires

    def need_service(self) -> bool:
        wear_sum = 0
        for tire in self.tires_state:
            wear_sum += tire
        if wear_sum >= 3:
            return True
        return False

# TODO 7: Making the Serviceable Interface
class Serviceable(ABC):
    """Serviceable Interface, checks if a Car will be serviceable or not"""

    @abstractmethod
    def need_service(self, engine, battery) -> bool:
        """Makes sure that the implementation will check if the battery and engine are serviceable"""
        pass


# TODO 8: Making the Car Interface
class Car(Serviceable):
    """Car Interface"""

    def __init__(self, Engine, Battery,Tires):
        """Takes Engine and Battery as Constructor Parameters"""
        self.engine = Engine
        self.battery = Battery
        self.tires = Tires

    def need_service(self, engine, battery) -> bool:
        if self.engine.need_service() or self.battery.need_service() or self.tires.need_service():
            return True
        return False


# TODO 9: Create Car Factory
class CarFactory:
    date = date.today().year

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,tire_state) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_state)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,tire_state) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tire_state)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date,warning_indicator_status,tire_state) -> Car:
        engine = SternmanEngine(warning_indicator_status)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(tire_state)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,tire_state) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire_state)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,tire_state) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tire_state)
        car = Car(engine, battery, tires)
        return car

