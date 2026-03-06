"""
Write a unittest assertion that will fail if value is not None.
"""

class TestSomething(unittest.TestCase):
    def test_value_is_none(self):
        value = None    
        self.assertIsNone(value, "Expected value to be None, but it was not.")