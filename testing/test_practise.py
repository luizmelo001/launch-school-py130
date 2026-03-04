import unittest

def greet(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    return f"Hello, {name}!"

class TestGreet(unittest.TestCase):
    def test_normal_name(self):
        self.assertEqual(greet("Mathias"), "Hello, Mathias!")

    def test_empty_string(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            greet(123)  
        with self.assertRaises(TypeError):
            greet(None)
        with self.assertRaises(TypeError):
            greet(["Mathias"])
    
    def test_whitespace_name(self):
        self.assertEqual(greet("   "), "Hello,    !")

if __name__ == "__main__":
    unittest.main()