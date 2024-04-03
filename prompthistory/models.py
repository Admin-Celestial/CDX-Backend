from django.db import models

class SmartqueryHistory(models.Model):
    q_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    response = models.CharField(max_length=10000)
    U_ID = models.IntegerField(null=True)
    created_on = models.DateTimeField()
    STATUS_CHOICES = (
        ('0', 'Dis-liked'),
        (None, 'Not Responded'),
        ('1', 'Liked'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=None , null=True)






    class Meta:
        managed = False
        db_table = 'smartquery_chathistory'
