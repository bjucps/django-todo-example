from django.test import Client, TestCase
from django.contrib.auth.models import User
from todo.models import Todo
import mock

class FakeNow:
    def __init__(self, day):
        self.day = day

    def weekday(self):
        return self.day


def fake_datetime_not_friday():
    return FakeNow(3)


def fake_datetime_friday():
    return FakeNow(4)


# sample unit tests
class TodoUnitTestCases(TestCase):
    @mock.patch("datetime.datetime")
    def test_completed_not_friday(self, mock_datetime):
        todo = Todo(done=False, description="a simple test")
        self.assertEqual(todo.done, False)
        mock_datetime.now.side_effect = fake_datetime_not_friday
        todo.markCompleted()
        self.assertEqual(todo.done, True)

    @mock.patch("datetime.datetime")
    def test_completed_friday(self, mock_datetime):
        todo = Todo(done=False, description="a simple test")
        self.assertEqual(todo.done, False)
        mock_datetime.now.side_effect = fake_datetime_friday
        todo.markCompleted()
        self.assertEqual(todo.done, False)

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
