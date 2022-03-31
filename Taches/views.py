from django.shortcuts import  render
from Taches.models import Affectation, Tache
from Taches.forms import AddTacheForm, UserTachesForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView 

def taches(request):
	taches = Tache.objects.all()

	return render(request, 'taches/taches_list.html', {'taches':taches})



def UsersTaches(request):
	Users_Taches = Affectation.objects.all()

	return render(request, 'taches/Users_Taches.html', {'Users_taches':Users_Taches})

class UserTacheCreateView(BSModalCreateView):
    template_name = 'taches/add_user_tache.html'
    form_class = UserTachesForm
    success_message = 'Success: new task was created.'
    success_url = reverse_lazy('UsersTaches')

class TacheCreateView(BSModalCreateView):
    template_name = 'taches/add_tache.html'
    form_class = AddTacheForm
    success_message = 'Success: tache was created.'
    success_url = reverse_lazy('dashboard')
    







