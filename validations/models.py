from django.db import models


class Validation(models.Model):
    val_id = models.AutoField(primary_key=True)
    U_ID = models.IntegerField(null=True)
    Question = models.TextField(null = True)
    Answer = models.TextField(null = True)
    Suggested_ans = models.TextField(null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('0', 'Disapproved'),
        (None, 'Not Validated'),
        ('1', 'Validated'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=None , null=True)

