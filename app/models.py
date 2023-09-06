from django.db import models

# Create your models here.
class Student(models.Model):
    rollnumber=models.IntegerField()
    name=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25,blank=False,null=False)
    def __str__(self):
        return self.name
       
class StudentFamily(models.Model):
    name=models.ForeignKey(Student,on_delete=models.CASCADE)
    father_name=models.CharField(max_length=20)
    mother_name=models.CharField(max_length=30)
    emergency=models.IntegerField()
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.father_name