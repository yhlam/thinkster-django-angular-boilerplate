from django.db import models


class Post(models.Model):
    author = models.ForeignKey('authentication.Account')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
