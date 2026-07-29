from django.db import models
from .user import User


class Post(models.Model):
    title_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    cont = models.TextField(max_length=500)
    date = models.DateField()
    summary = models.TextField(max_length=200)

    summary_generated_at = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE, 
                             related_name='posts')

    def __str__(self):
        return self.title