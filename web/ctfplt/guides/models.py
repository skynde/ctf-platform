from django.db import models

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Genre(models.Model):
    name = models.CharField(max_length=64, default="")
    def __str__(self):
        return self.name

class Article(models.Model):
    genre = models.ForeignKey(Genre)
    title = models.CharField(max_length=128, default="")
    index = models.IntegerField(default = 0)
    _text = MarkdownxField(default="")

    def __str__(self):
        return "[" + self.genre.name + "] " + str(self.index) + ": " + self.title

    @property
    def text(self):
        return markdownify(self._text)


