import unittest
# from warmUpOne import WarmUpOne
from warmUpOne import * 

class TestWarmUp1(unittest.TestCase):

    def test_sleep_in_True(self):
        result = sleep_in(True, True)
        self.assertEquals(result, True)
        
    def test_sleep_in_weekend_vacation(self):
        result = sleep_in(False, True)
        self.assertEquals(result, True)


# is this file being run directly by python or imported
if __name__ == '__main__':
    unittest.main()