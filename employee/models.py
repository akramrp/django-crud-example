from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    # file      = forms.FileField() # for creating file input 
    # pub_date  = models.DateField()
    # content   = models.TextField()
    # id = models.AutoField(primary_key=True)

    class Meta:  
        db_table = "employee"  