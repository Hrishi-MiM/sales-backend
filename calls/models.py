from django.db import models
from assistant.models import Assistant

# Create your models here.
class Call(models.Model):
    id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=255)
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session_name

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    call = models.ForeignKey(Call, related_name='logs', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)  # Can be 'Sys' or 'client_name'
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Log for {self.call.session_name} by {self.user}"
