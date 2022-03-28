from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    User_type=(
('1', 'Chef Du Projet'),
('2', 'Utilisateur'),
('3', 'Client'),

 )  
    Type = models.CharField(max_length=100,choices=User_type )
    permissions = (
                       ("view_vote_office", "can view vote office"),
                       ("find_vote", "can find vote"),
                      )