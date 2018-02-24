from django.db import models

# Create your models here.
class directional(models.Model):
    fgid = models.CharField(max_length=3)
    directionalStatement = models.TextField()
    def __str__(self):
        return self.fgid
class Groups(models.Model):
    fgid = models.CharField(max_length=3)
    foodgroup = models.TextField()
    fgcat_id = models.CharField(max_length=2)
    fgcat = models.TextField()
    def __str__(self):
        return self.fgcat_id

class Foods(models.Model):
    fgid = models.CharField(max_length=3)
    fgcat_id = models.CharField(max_length=2)
    srvg_sz = models.TextField()
    food = models.TextField()
    def __str__(self):
        return self.fgcat_id
GENDER = (
    ('Male', 'Male'),
    ('Female','Female'),
)
AGES = (
    ('2 to 3','2 to 3'),
    ('4 to 8','4 to 8'),
    ('9 to 13','9 to 13'),
    ('14 to 18','14 to 18'),
    ('19 to 30','19 to 30'),
    ('31 to 50','31 to 50'),
    ('51 to 70','51 to 70'),
    ('71+','71+'),
)

class Form(models.Model):
    gender = models.CharField(max_length=10,choices=GENDER)
    age = models.CharField(max_length=10,choices=AGES)

class Serving(models.Model):
    fgid = models.CharField(max_length=3)
    gender = models.CharField(max_length=8)
    ages = models.TextField()
    servings = models.TextField()

    def __str__(self):
        return self.gender

