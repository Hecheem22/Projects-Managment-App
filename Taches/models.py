from django.db import models
from Projects.models import Project
from Accounts.models import User

class Tache(models.Model):
   STATUS = (
		
			('uncompleted', 'uncompleted'),
			('complete', 'complete'),
			)
   Name = models.CharField(max_length=255 , verbose_name='Nom')    
   Description = models.TextField( max_length=800 , verbose_name='Description du tache')
   StartDate  = models.DateField(  max_length=100, auto_now=False, auto_now_add=False , verbose_name='Date de début') 
   EndDate = models.DateField( max_length=100, auto_now=False, auto_now_add=False, verbose_name='Date de fin')
   Status = models.CharField(max_length=200, null=True, choices=STATUS)
   Project = models.ForeignKey( Project , null=True, on_delete=models.SET_NULL  )



class Affectation(models.Model):
   Tache=models.ForeignKey( Tache , null=True, on_delete=models.SET_NULL  )
   User = models.ForeignKey( User , null=True, on_delete=models.SET_NULL  )


   
  