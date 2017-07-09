from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Tag(models.Model):
    name = models.CharField(max_length=16, default="")
    def __str__(self):
        return self.name

class Problem(models.Model):
    title = models.CharField(max_length=128, default="")
    flag = models.CharField(max_length=64, default="")
    tags = models.ManyToManyField(Tag, blank=True)
    score = models.IntegerField(default = 0)
    unlockProblems = models.ManyToManyField("self", blank=True)
    _description = MarkdownxField(default="")
    _hint = MarkdownxField(default="")
    def __str__(self):
        return self.title

    @property
    def description(self):
        return markdownify(self._description)
    @property
    def hint(self):
        return markdownify(self._hint)

