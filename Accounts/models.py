from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    User_type=(
('1', 'Chef Du Projet'),
('2', 'Employee'),
('3', 'Client'),

 )  
    Type = models.CharField(max_length=100,choices=User_type )
    def get_delete_user_url(self):
        return reverse('delete_user', kwargs={'pk': self.id})
    def get_edit_user_url(self):
        return reverse('edit_user', kwargs={'pk': self.id})


    def get_no_project_manager_no_client (self):
        return self.Type=='2'