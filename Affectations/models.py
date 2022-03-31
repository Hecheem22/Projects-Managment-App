from django.db import models
from Accounts.models import User
from Taches.models import Tache





class Affecations(models.Model):
    Tache = models.ForeignKey(Tache  , null=True, on_delete=models.SET_NULL  )
    User = models.ForeignKey(User  , null=True, on_delete=models.SET_NULL  )
