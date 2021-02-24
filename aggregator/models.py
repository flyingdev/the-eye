from django.db import models

# Create your models here.


class Event(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['session_id', 'timestamp'], name='unique event for session'),
            models.Index(fields=['session_id'], name='session index'),
            models.Index(fields=['category'], name='category index'),
            models.Index(fields=['timestamp'], name='timestamp index'),
        ]

    session_id = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    data = models.JSONField(help_text='JSON data')
    timestamp = models.DateTimeField(help_text='Event occurred timestamp')
    created_at = models.DateTimeField(auto_now=True)
