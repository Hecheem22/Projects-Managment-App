import django_tables2 as tables
from .models import Affectation



class TachesTable(tables.Table):
   
 class Meta:
        model = Affectation
        attrs = {'id': 'taches_table',
        'class' : 'table table-sm table-responsive-sm table-hover text-nowrap table-striped table-bordered'}
        template_name = "django_tables2/bootstrap.html"
        fields = ("id" ,  "User" , "Tache"   )
        sequence = ('id',  "User" , "Tache"    )
        