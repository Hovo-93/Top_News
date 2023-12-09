from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news_images/')
    text = models.TextField()

    def __str__(self):
        return self.title


class TopNewsLink(models.Model):
    url = models.URLField(unique=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
