from django.db import models
from django.contrib.auth.models import AbstractUser
from problems.models import Problem
from django.utils import timezone

class Affiliate(models.Model):
    name = models.CharField(max_length=64, default="")
    solvedProblems = models.ManyToManyField(Problem, blank=True)
    score = models.IntegerField(default = 0)
    def __str__(self):
        return self.name

class User(AbstractUser):
    userID = models.IntegerField(default = 0)
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE, default=None, blank=True, null=True)
    score = models.IntegerField(default = 0)
    lastSubmitDatetime = models.DateTimeField(default=timezone.now)

    solvedProblems = models.ManyToManyField(Problem, blank=True, related_name="solvedProblems")
    noHintSolvedProblems = models.ManyToManyField(Problem, blank=True, related_name="noHintSolvedProblems")
    hintedProblems = models.ManyToManyField(Problem, blank=True, related_name="hintedProblems")
    availableProblems = models.ManyToManyField(Problem, blank=True, related_name="availableProblems")

    def addSolvedProblems(self, problem):
        self.solvedProblems.add(problem)
        self.save()
    def addNoHintedSolvedProblems(self, problem):
        self.noHintSolvedProblems.add(problem)
        self.save()
    def addHintedProblems(self, problem):
        self.hintedProblems.add(problem)
        self.save()
    def addAvailableProblems(self, problems):
        for problem in problems:
            self.availableProblems.add(problem)
        self.save()

class SubmittedHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, default=None, blank=True, null=True)
    isCorrect = models.BooleanField(default = False)
    withHint = models.BooleanField(default = False)
    submitDatetime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        ret = self.user.username + "(" + self.problem.title + "): "
        if self.isCorrect:
            ret += "Correct"
        else:
            ret += "Wrong"
        if self.withHint:
            ret += ", with the hint"
        return ret
