from django.shortcuts import redirect , render
from Taches.models import Tache
from Taches.forms import AddTacheForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from bootstrap_modal_forms.generic import BSModalCreateView 

def taches(request):
	taches = Tache.objects.all()

	return render(request, 'taches/taches_list.html', {'taches':taches})







class TacheCreateView(BSModalCreateView):
    template_name = 'taches/add_tache.html'
    form_class = AddTacheForm
    success_message = 'Success: tache was created.'
    success_url = reverse_lazy('dashboard')
    







