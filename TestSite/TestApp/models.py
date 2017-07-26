from django.db import models
from django.utils import timezone
import ast

# Create your models here.

class Hi(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=10)
    body = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        null=True, blank=True
    )

    def publish(self):
        self.published_date = timezone.now
        self.save

    def __str__(self):
        return self.title