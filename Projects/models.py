from django.db import models


from django.db import models
from django.urls import reverse
from Accounts.models import User






class Project(models.Model):

  STATUS = (
		
			('uncompleted', 'uncompleted'),
			('completed', 'completed'),
			)
  
  Title = models.CharField(max_length=255)
  Description = models.TextField( max_length=800 )
  StartDate  = models.DateField(  max_length=100, auto_now=False, auto_now_add=False , verbose_name='Start Date') 
  EndDate = models.DateField( max_length=100, auto_now=False, auto_now_add=False, verbose_name='End Date')
  ProjectManager = models.ForeignKey(User  , null=True, on_delete=models.SET_NULL , verbose_name='Project Manager' )
  Status = models.CharField(max_length=200, null=True, choices=STATUS , default='uncompleted')


  def get_absolute_url(self):
      return reverse('project_details', kwargs={'pk': self.id})
  def get_delete_projeect_url(self):
        return reverse('delete_projeect', kwargs={'pk': self.id})
  def get_edit_project_url(self):
        return reverse('edit_project', kwargs={'pk': self.id})