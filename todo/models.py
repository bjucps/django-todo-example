from django.db import models
import datetime


FRIDAY = 4


class Todo(models.Model):
    done = models.BooleanField(default=False)
    description = models.TextField()

    def markCompleted(self):
        if datetime.datetime.now().weekday() != FRIDAY:
            self.done = True
