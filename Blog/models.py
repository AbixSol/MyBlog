from django.contrib.auth.models import User
from django.db import models

# Create your models here.

SHORT_TEXT_LEN = 1000


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['-date', ]

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text
