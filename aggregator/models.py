from django.db import models

# Create your models here.


class Event(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['session_id', 'timestamp'], name='unique event for session'),
        ]

    session_id = models.CharField(max_length=256, db_index=True)
    category = models.CharField(max_length=256, db_index=True)
    name = models.CharField(max_length=256)
    data = models.JSONField(help_text='JSON data')
    timestamp = models.DateTimeField(help_text='Event occurred timestamp', db_index=True)
    created_at = models.DateTimeField(auto_now=True)
