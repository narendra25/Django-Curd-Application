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
class Album(models.Model):
    artist = models.ForeignKey(Student,default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()