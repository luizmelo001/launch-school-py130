"""
Write a unittest assertion that will fail if value.lower() does not return 'xyz'.
"""

import unittest

class TestSomething(unittest.TestCase):
    def test_value_lower(self):
        value = "XYZ"
        self.assertEqual('xyz', value.lower())

if __name__ == '__main__':    
    unittest.main()