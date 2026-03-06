import unittest

class TestSomething(unittest.TestCase):
    def test_value_is_odd(self):
        value = 3
        self.assertTrue(value % 2 == 1, "Value should be odd")

if __name__ == '__main__':
    unittest.main()
