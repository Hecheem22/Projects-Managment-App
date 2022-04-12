from Taches.models import Affectation, Tache
from django import forms 
from bootstrap_modal_forms.forms import BSModalModelForm
from Accounts.models import User



class AddTacheForm(BSModalModelForm):  
    class Meta:  
        model = Tache
        fields = ['Name', 'Description', 'StartDate' , 'EndDate' , 'Status' ] 
        widgets = { 'Name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'Description': forms.Textarea(attrs={ 'class': 'form-control' }),
            'StartDate': forms.DateInput(attrs={ 'class': 'form-control' , 'type' : 'date' }),
            'EndDate': forms.DateInput(attrs={ 'class': 'form-control' , 'type' : 'date' }),
            'Status': forms.Select(),}




class UserTachesForm(BSModalModelForm):
    User = forms.Select()
    Tache = forms.Select()
    class Meta:
        model= Affectation
        fields=['User' , 'Tache']
        
                         