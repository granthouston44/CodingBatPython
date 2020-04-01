import unittest
from warmUpOne import WarmUpOne 

class TestWarmUp1(unittest.TestCase):

    def test_sleep_in(self):
        result = WarmUpOne.sleep_in(True, True)
        self.assertEquals(result, True)
        
    def test_sleep_in_weekend_vacation(self):
        result = WarmUpOne.sleep_in(False, True)
        self.assertEquals(result, True)


# is this file being run directly by python or imported
if __name__ == '__main__':
    unittest.main()