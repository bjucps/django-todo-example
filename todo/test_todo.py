from django.test import Client, TestCase
from django.contrib.auth.models import User
from todo.models import Todo


# sample unit tests
class TodoUnitTestCases(TestCase):
    def test_completed(self):
        todo = Todo(done=False, description="a simple test")
        self.assertEqual(todo.done, False)
        todo.markCompleted()
        self.assertEqual(todo.done, True)

# sample integration test


class TodoIntegrationTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='temporary',
            email='temporary@gmail.com',
            password='temporary')

    def test_create_edit_delete(self):
        c = Client()
        logged_in = c.login(username="temporary", password="temporary")
        self.assertEqual(logged_in, True)
        response = c.post('/todo/todo/new',
                          {'done': False, 'description': "a simple test"})
        self.assertLess(response.status_code, 400)
        todo = Todo.objects.get(description="a simple test")
        self.assertIsNotNone(todo)
        self.assertEqual(todo.done, False)
        self.assertEqual(todo.description, "a simple test")

        response = c.post(
            f'/todo/todo/{todo.id}/edit', {'done': True, 'description': "a simple test"})
        self.assertLess(response.status_code, 400)
        todo = Todo.objects.get(description="a simple test")
        self.assertEqual(todo.done, True)
        self.assertEqual(todo.description, "a simple test")

        response = c.post(f'/todo/todo/{todo.id}/delete')
        try:
            todo = Todo.objects.get(description="a simple test")
            self.assertTrue(True, False)  # we should not have gotten here
        except Todo.DoesNotExist:
            pass

        # cleanup
        Todo.objects.all().delete()
