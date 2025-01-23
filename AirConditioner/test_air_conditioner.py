import unittest
import air_conditioner


class AirConditionerTest(unittest.TestCase):
    def test_that_ac_is_off(self):
        result = air_conditioner.is_off()
        self.assertTrue(result)


    def test_that_ac_is_on(self):
        result = air_conditioner.is_on()
        self.assertTrue(result)

    def test_that_ac_increases(self):
        result = air_conditioner.it_increases()
        self.assertTrue(result)

    def test_that_ac_decreases(self):
        result = air_conditioner.it_decreases()
        self.assertTrue(result)

    def test_that_when_ac_is_on_before_increase(self):
        result = air_conditioner.set_temperature(16)
        

if __name__ == '__main__':
    unittest.main();
