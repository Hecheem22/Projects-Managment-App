from django.db import models
from Projects.models import Project
from Accounts.models import User

class Tache(models.Model):
   STATUS = (
		
			('uncompleted', 'uncompleted'),
			('completed', 'completed'),
			)
   Name = models.CharField(max_length=255 )    
   Description = models.TextField( max_length=800 )
   StartDate  = models.DateField(  max_length=100, auto_now=False, auto_now_add=False ) 
   EndDate = models.DateField( max_length=100, auto_now=False, auto_now_add=False)
   Status = models.CharField(max_length=200, null=True, choices=STATUS)
   Project = models.ForeignKey( Project , null=True, on_delete=models.SET_NULL  )
   
   def __str__(self):
       return self.Name
       
   
  

class Affectation(models.Model):
   Tache =models.ForeignKey( Tache , null=True, on_delete=models.SET_NULL)
   User = models.ForeignKey( User , null=True, on_delete=models.SET_NULL )

