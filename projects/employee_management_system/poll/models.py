from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    titile = models.TextField(null=True, blank=True)
    status = models.CharField(default='inactive', max_length=10)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titile

class Choice(models.Model):
    question = models.ForeignKey('poll.Question', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    