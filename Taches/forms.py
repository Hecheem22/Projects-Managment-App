from Taches.models import Tache
from django import forms 
from bootstrap_modal_forms.forms import BSModalModelForm

class AddTacheForm(BSModalModelForm):  
    class Meta:  
        model = Tache
        fields = ['Name', 'Description', 'StartDate' , 'EndDate' , 'Status' , 'Project'] 
        widgets = { 'Name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'Description': forms.Textarea(attrs={ 'class': 'form-control' }),
            'StartDate': forms.DateInput(attrs={ 'class': 'form-control' , 'type' : 'date' }),
            'EndDate': forms.DateInput(attrs={ 'class': 'form-control' , 'type' : 'date' }),
             'Status': forms.Select(),
              'Project': forms.Select()

             }