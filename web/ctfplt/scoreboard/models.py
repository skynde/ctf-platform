from django.db import models
from problems.models import Problem
from accounts.models import User

class PostedHistory(models.Model):
    postedDateTime = models.DateTimeField()
    postedUser = models.ForeignKey(User)
    postedProblem = models.ForeignKey(Problem)
    result = models.BooleanField()

