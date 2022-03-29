from .models import Project
from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms



class AddProjectForm(BSModalModelForm):
    Title = forms.CharField(
        widget=forms.TextInput(
            
        ))
    Description = forms.CharField(
        widget=forms.Textarea(
            
        ))
    StartDate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                
                "type": "date"
            }
        ))
    EndDate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                
                "type": "date"
            }
        ))

    ProjectManager = forms.Select()   
    Status = forms.Select()

    class Meta:
        model = Project
        fields = ("Title", "Description", "StartDate", "EndDate" , "ProjectManager" , "Status")