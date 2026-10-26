import unittest
from app import app, lists

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        lists.clear()
        import app as app_module
        app_module.next_list_id = 1
        app_module.next_task_id = 1

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'My To-Do Lists', response.data)

    def test_create_list(self):
        response = self.client.post('/lists', data={'name': 'Groceries'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Groceries', response.data)

    def test_add_task(self):
        self.client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
        response = self.client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Finish report', response.data)

    def test_toggle_task(self):
        self.client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
        self.client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
        response = self.client.post('/lists/1/tasks/1/toggle', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mark Incomplete', response.data)

    def test_delete_task(self):
        self.client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
        self.client.post('/lists/1/tasks', data={'description': 'Finish report'}, follow_redirects=True)
        response = self.client.post('/lists/1/tasks/1/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Finish report', response.data)

    def test_delete_list(self):
        self.client.post('/lists', data={'name': 'Work'}, follow_redirects=True)
        response = self.client.post('/lists/1/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Work', response.data)

if __name__ == '__main__':
    unittest.main()
