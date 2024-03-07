from django.db import models

# Create your models here.
class Admin(models.Model):
    id : models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,blank=False,unique=True)
    password=models.CharField(max_length=12,blank=False)
    class Meta:
        db_table = "ttmadmin_table"
