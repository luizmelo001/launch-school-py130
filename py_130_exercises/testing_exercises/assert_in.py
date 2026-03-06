
"""
Write a unittest assertion that will fail if the 'xyz' is not in the list lst.
"""

import unittest


class TestSomething(unittest.TestCase):
    def test_xyz_in_list(self):
        lst = ['abc', 'def', 'xyz']
        self.assertIn('xyz', lst, "Expected 'xyz' to be in the list, but it was not.")


if __name__ == '__main__':   
    unittest.main()

