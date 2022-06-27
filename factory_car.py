import datetime
from abc import ABC, abstractmethod,abstractproperty
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
    last_service_mileage = 0  # some int representing the number of miles since last service
    current_mileage = 0  # the mileage (int) at which the car currently is at.

    def need_service(self) -> bool:
        """Checks if mileage is greater than miles necessary for service, in this case 30_000"""
        if (CapuletEngine.current_mileage - CapuletEngine.last_service_mileage) >= 30_000:
            return True
        return False

class WilloughbyEngine(Engine):
    """Willoughby Engine is implementation of the Engine Abstract Class"""
    last_service_mileage = 0
    current_mileage = 0

    def need_service(self) -> bool:
        """Checks if mileage is greater than miles necessary for service, in this case 60_000"""
        if (CapuletEngine.current_mileage - CapuletEngine.last_service_mileage) >= 60_000:
            return True
        return False

class SternmanEngine(Engine):
    """Sternman Engine is implementation of the Engine Abstract Class"""
    warning_indicator_status = False  # In this case warning indicator status determines whether servicing is necessary

    def need_service(self) -> bool:
        """Checks if services are necessary, which happens only if warning indicator is on / denoted by True"""
        if SternmanEngine.warning_indicator_status:
            return True
        return False

#TODO 3: Making the Battery Interface
class Battery(ABC):
    """Battery Interface for implementation"""

    @abstractmethod
    def need_service(self) -> bool:
        """Checks if the battery needs service"""

#TODO 4: Making Battery Implementations
class SpindlerBattery(Battery):
    """Spindler Battery is an implementation of the Battery implementation"""
    current_date = date.today().year #Getting current date
    last_service_date = 2022 #Getting the year of Battery's last service

    def need_service(self) -> bool:
        """Battery needs service if it has not been serviced in 2 years"""
        if (SpindlerBattery.current_date - SpindlerBattery.last_service_date) >= 2:
            return True
        return False

class NubbinBattery(Battery):
    """Spindler Battery is an implementation of the Battery implementation"""
    current_date = date.today().year #Getting current date
    last_service_date = 2022 #Getting the year of Battery's last service

    def need_service(self) -> bool:
        """Battery needs service if it has not been serviced in 4 years"""
        if (NubbinBattery.current_date - NubbinBattery.last_service_date) >= 4:
            return True
        return False

#TODO 5: Making the Serviceable Interface
class Serviceable(ABC):
    """Serviceable Interface, checks if a Car will be serviceable or not"""
    @abstractmethod
    def need_service(self,engine,battery) -> bool:
        """Makes sure that the implementation will check if the battery and engine are serviceable"""

#TODO 6: Making the Car Interface
class Car(Serviceable):
    """Car Interface"""
    def __init__(self,Engine,Battery):
        """Takes Engine and Battery as Constructor Parameters"""
        self.engine = Engine
        self.battery = Battery

    def need_service(self,engine,battery) -> bool:
        if self.engine.need_service or self.battery.need_service:
            return True
        return False

#TODO 7: Create Car Factory
class CarFactory:
    date = date.today().year

    def create_calliope(current_date = date, last_service_date = date, current_mileage = 0, last_service_mileage = 0) -> Car():
        calliope = Car(CapuletEngine,SpindlerBattery)
        calliope.battery.last_service_date = last_service_date
        calliope.engine.last_service_mileage = last_service_mileage
        calliope.current_mileage = current_mileage
        return calliope

    def create_glissade(current_date = date, last_service_date = date, current_mileage = 0, last_service_mileage = 0) -> Car():
        glissade = Car(WilloughbyEngine,SpindlerBattery)
        glissade.battery.last_service_date = last_service_date
        glissade.engine.last_service_mileage = last_service_mileage
        glissade.current_mileage = current_mileage
        return glissade

    def create_palindrome(current_date = date, last_service_date = date, warning_light_on = True) -> Car():
        pallindrome = Car(SternmanEngine,SpindlerBattery)
        pallindrome.battery.last_service_date = last_service_date
        pallindrome.engine.warning_indicator_status = warning_light_on
        return pallindrome

    def create_rorschach(current_date = date, last_service_date = date, current_mileage = 0, last_service_mileage = 0) -> Car():
        rorschach = Car(WilloughbyEngine,NubbinBattery)
        rorschach.battery.last_service_date = last_service_date
        rorschach.engine.last_service_mileage = last_service_mileage
        rorschach.current_mileage = current_mileage
        return rorschach

    def create_thovex(current_date = date, last_service_date = date, current_mileage = 0, last_service_mileage = 0) -> Car():
        thovex = Car(CapuletEngine,NubbinBattery)
        thovex.battery.last_service_date = last_service_date
        thovex.engine.last_service_mileage = last_service_mileage
        thovex.current_mileage = current_mileage
        return thovex







