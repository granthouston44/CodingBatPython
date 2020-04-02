import unittest
# from warmUpOne import WarmUpOne
from warmUpOne import * 

class TestWarmUp1(unittest.TestCase):

# Sleep in 
    def test_sleep_in_True(self):
        result = sleep_in(True, True)
        self.assertEquals(result, True)
        
    def test_sleep_in_weekend_vacation(self):
        result = sleep_in(False, True)
        self.assertEquals(result, True)

# Monkey Trouble
    def test_monkey_trouble_true(self):
        result = monkey_trouble(True, True)
        self.assertEquals(result, True)

        result2 = monkey_trouble(False, False)

    def test_monkey_trouble_false(self):
        result = monkey_trouble(True, False)
        self.assertEquals(result, False)

# sum double

    def test_sum_double_1_2(self):
        result = sum_double(1,2)
        self.assertEquals(result, 3)

    def test_sum_double_2_2(self):
        result = sum_double(2,2)
        self.assertEquals(result, 8)

#diff21

    def test_diff21_under21(self):
        result = diff21(10)
        self.assertEquals(result, 11)

    def test_diff21_over21(self):
        result = diff21(25)
        self.assertEquals(result, 8)

#parrot trouble

    def test_in_trouble(self):
        result = parrot_trouble(True, 6)
        self.assertEquals(result, True)

    def test_not_in_trouble(self):
        result = parrot_trouble(False, 6)
        self.assertEquals(result, False)

#makes 10

    def test_sum_is_ten(self):
        result = makes10(5,5)
        self.assertEquals(result, True)

    def test_a_is_ten(self):
        result = makes10(10, 3)
        self.assertEquals(result, True)

    def test_false(self):
        result = makes10(5,3)
        self.assertEquals(result, False)

# is this file being run directly by python or imported
if __name__ == '__main__':
    unittest.main()