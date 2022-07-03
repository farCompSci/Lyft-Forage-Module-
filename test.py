import unittest
from datetime import date
from __init__ import *

#TODO 1: Running tests for the implementations of the Engine Class
class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine(self):
        engine = CapuletEngine(current_mileage=30_001,last_service_mileage=0)
        result = engine.need_service()
        self.assertTrue(result)

class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine(self):
        engine = WilloughbyEngine(current_mileage=20_000,last_service_mileage=10_000)
        result = engine.need_service()
        self.assertFalse(result)

class TestSternmanEngine(unittest.TestCase):
    def test_willoughby_engine(self):
        engine = SternmanEngine(warning_indicator_status=True)
        result = engine.need_service()
        self.assertTrue(result)


#TODO 2: Running tests for the implementation of the Battery Class

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery(self):
        current_year = date.today().year
        battery = SpindlerBattery(current_date=current_year,last_service_date=current_year-4)
        result = battery.need_service()
        self.assertTrue(result)

class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery(self):
        current_year = date.today().year
        battery = NubbinBattery(current_date=current_year,last_service_date=current_year-3)
        result = battery.need_service()
        self.assertFalse(result)

#TODO 3: Running Tires Implementation Test

class TestCarriganTires(unittest.TestCase):
    def test_carrigan_tires(self):
        tire_test_array = [0,0,1,0]
        tires = CarriganTires(tires_state=tire_test_array)
        result = tires.need_service()
        self.assertTrue(result)

class TestOctoprimeTires(unittest.TestCase):
    def test_octoprime_tires(self):
        tire_test_array = [1,1,0,1]
        tires = OctoprimeTires(tires_state=tire_test_array)
        result = tires.need_service()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
