"""
Write a test that will fail if lst and the return value of lst.process are different objects.
"""

import unittest

class MyList:
    def process(self):
        return self

class TestMyList(unittest.TestCase):
    def test_process_returns_same_object(self):
        lst = MyList()
        result = lst.process()
        self.assertIs(lst, result, "The process method should return the same object")

unittest.main()