from django.db import models

# Create your models here.
class ChatHistory(models.Model):
    
    # question = models.CharField(max_length = 500)
    q_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length = 500)
    response = models.CharField(max_length=10000)
    U_ID = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('0', 'Dis-liked'),
        (None, 'Not Responded'),
        ('1', 'Liked'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=None , null=True)

    def __str__(self):
        return f'Response for: {self.question}'
