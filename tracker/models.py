from django.db import models


class Request(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Comment(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=128)
    body = models.CharField(max_length=512)
    datetime = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['datetime']
