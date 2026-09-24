import unittest
from app import app, todo_lists

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        todo_lists.clear()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'To-Do List Web App', response.data)

    def test_create_list(self):
        response = self.client.post('/lists', data={'name': 'Work Tasks'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Work Tasks', response.data)

    def test_add_task(self):
        self.client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
        response = self.client.post('/lists/1/tasks', data={'text': 'Buy milk'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Buy milk', response.data)

if __name__ == '__main__':
    unittest.main()
