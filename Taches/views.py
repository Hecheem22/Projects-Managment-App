from django.shortcuts import  render
from Taches.models import Affectation, Tache
from Taches.forms import AddTacheForm, UserTachesForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView 
from django.views.generic.base import View
from Taches.tables import TachesTable

def taches(request):
	taches = Tache.objects.all()

	return render(request, 'taches/taches_list.html', {'taches':taches})



class UsersTachesTable(View):
 def get(self,request):
        queryset = Affectation.objects.all()
        Taches_Table = TachesTable(queryset)
       
        context = {'view_taches':Taches_Table }
        return render(request, 'taches/users_taches.html', context)
        


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
    







