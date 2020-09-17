from django.db import models


class Todo(models.Model):
    done = models.BooleanField(default=False)
    description = models.TextField()

    def markCompleted(self):
        self.done = True
