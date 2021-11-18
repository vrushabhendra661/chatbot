from django.db import models

# Create your models here.

class Stupid(models.Model):
    """
    this class defines model to count number of Stupid buttons clicks
    """
    stupidcount = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')

    def __str__(self) -> str:
        return "Stupid count is " + str(self.stupidcount)

class Fat(models.Model):
    """
    this class defines model to count number of Fat buttons clicks
    """
    fatcount = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
    def __str__(self) -> str:
        return "Fat count is " + str(self.fatcount) 

class Dumb(models.Model):
    """
    this class defines model to count number of Stupid buttons clicks
    """
    dumbcount = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')

    def __str__(self) -> str:
        return "Dumb count is " + str(self.dumbcount)