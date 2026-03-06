"""
Write a test that will fail if 'xyz' is one of the elements in the list lst.
"""

import unittest


class TestSomething(unittest.TestCase):
    def test_xyz_not_in_list(self):
        lst = ['abc', 'def', 'ghi']  # Example list
        self.assertNotIn('xyz', lst, "The element 'xyz' should not be in the list")

if __name__ == '__main__':
    unittest.main()