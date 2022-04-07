from statistics import mode
from django.db import models

class PlayGround(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
       return self.title

    def snipet(self):
        return self.content[:2] + "...."
