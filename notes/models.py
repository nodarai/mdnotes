from django.db import models


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)