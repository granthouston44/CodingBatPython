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


# is this file being run directly by python or imported
if __name__ == '__main__':
    unittest.main()