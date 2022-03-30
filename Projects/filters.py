from dataclasses import fields
from unicodedata import name
import django_filters
from .models import *
from django_filters import DateFilter 

class ProjectFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="StartDate", lookup_expr='gte' , label='StartDate')
    end_date = DateFilter(field_name="EndDate", lookup_expr='lte' , label='EndDate')

    class Meta:
        model =Project
        fields = '__all__'
        exclude = [ 'ProjectManager' , 'Status' ,'Description' , 'StartDate' , 'EndDate']
       