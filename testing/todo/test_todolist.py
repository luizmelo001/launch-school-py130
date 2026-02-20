import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    # your tests go here
    def test_length(self):
        self.assertEqual(len(self.todos), 3)

    def test_to_list(self):
        self.assertEqual(self.todos.to_list(), [self.todo1, self.todo2, self.todo3])

    def test_first(self):
        self.assertEqual(self.todos.first(), self.todo1)

    def test_last(self):
        self.assertEqual(self.todos.last(), self.todo3)

    def test_all_done(self):
        self.assertFalse(self.todos.all_done())
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add("Not a Todo")

    
        

if __name__ == "__main__":
    unittest.main()