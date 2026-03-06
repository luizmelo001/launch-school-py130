"""
Write a unittest assertion that will fail if value is not an instance of the Numeric class or one of its subclasses.
"""

import unittest

class Numeric:
    pass

class Integer(Numeric):
    pass

class TestNumeric(unittest.TestCase):
    def test_is_instance_of_numeric(self):
        value = Integer()  # Example value, you can replace it with any instance
        self.assertIsInstance(value, Numeric, "Value is not an instance of Numeric or its subclasses")  


if __name__ == '__main__':
    unittest.main()