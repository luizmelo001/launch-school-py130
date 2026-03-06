"""
Write a unittest assertion that will fail unless employee.hire() raises a NoExperienceError exception when an employee only has 2 years of experience.
"""

class NoExperienceError(Exception):
    pass

class Employee:
    def __init__(self, experience):
        self.experience = experience
        self.hired = False

    def hire(self):
        if self.experience < 3:
            raise NoExperienceError
        else:
            self.hired = True

import unittest

class TestEmployeeHiring(unittest.TestCase):
    def setUp(self):
        self.employee = Employee(experience=2)

    def test_hire_with_insufficient_experience(self):
        with self.assertRaises(NoExperienceError):
            self.employee.hire()

if __name__ == '__main__':
    unittest.main()