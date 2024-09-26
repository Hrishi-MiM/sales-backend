from django.db import models

class Assistant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    prompt = models.TextField()
    greeting_message = models.TextField()
    max_tokens = models.IntegerField()
    idle_timeout = models.IntegerField()
    max_idle_messages = models.IntegerField()
    idle_message = models.TextField()
    is_publish = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
