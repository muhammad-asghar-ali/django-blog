from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thumbnail
    # add author

    def __str__(self) -> str:
        return self.title

    # model methods
    def snippet(self) -> str:
        return self.body[:50] + '...'
