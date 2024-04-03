from django.db import models


class TempUserMaster(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=95, null=True)
#    password = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
#    role = models.CharField(max_length=55,null=True)
#    created_on = models.DateTimeField(auto_now_add=True)
#    created_by = models.CharField(max_length=255, null=True)
    status_toggle = models.BooleanField(default=True)
   



    class Meta:
        managed = False
        db_table = 'baseusermaster_user'
