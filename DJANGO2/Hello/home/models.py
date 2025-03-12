from django.db import models



#makemigration - create changes and store in a file
#migrate-apply the pending changes created by the makemkgration
#migrate-apply the pending changes created by the makemkgration
# Create your models here.
class Contect(models.Model):
    name =models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    
class Signup(models.Model):
    name =models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    password = models.CharField(max_length=12)
    

    def __str__(self):
        return self.name