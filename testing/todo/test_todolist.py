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

    def test_todo_at(self):
        self.assertEqual(self.todos.todo_at(1), self.todo2)

        with self.assertRaises(IndexError):
            self.todos.todo_at(5)

    def test_mark_done_at(self):
        self.todos.mark_done_at(0)
        self.assertTrue(self.todo1.done)

        with self.assertRaises(IndexError):
            self.todos.mark_done_at(5)

    def test_mark_undone_at(self):
        self.todos.mark_done_at(0)
        self.todos.mark_undone_at(0)
        self.assertFalse(self.todo1.done)

        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(5)

    def test_remove_at(self):
        self.todos.remove_at(1)
        self.assertEqual(len(self.todos), 2)
        self.assertEqual(self.todos.to_list(), [self.todo1, self.todo3])

        with self.assertRaises(IndexError):
            self.todos.remove_at(5)

    def test_str(self):
        expected_output = "----- Today's Todos -----\n[ ] Buy milk\n[ ] Clean room\n[ ] Go to the gym"
        self.assertEqual(str(self.todos), expected_output)

    def test_str_done_todo(self):
        string = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[X] Clean room\n"
            "[ ] Go to the gym"
        )
        self.todos.mark_done_at(1)
        self.assertEqual(string, str(self.todos))

    def test_each(self):
        titles = []
        def collect_titles(todo):
            titles.append(todo.title)

        self.todos.each(collect_titles)
        self.assertEqual(titles, ["Buy milk", "Clean room", "Go to the gym"])

    def test_select(self):
        selected = self.todos.select(lambda todo: todo.done)
        self.assertEqual(len(selected), 0)
    
        self.todos.mark_done_at(1)
        selected = self.todos.select(lambda todo: todo.done)
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected.first(), self.todo2)  
        
if __name__ == "__main__":
    unittest.main()