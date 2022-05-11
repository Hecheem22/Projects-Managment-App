
from django.shortcuts import  render
from Projects.models import Project
from Taches.models import  Tache
from Taches.forms import AddTacheForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView , BSModalReadView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('taches.view_tache', raise_exception=True)
def taches(request):
	taches = Tache.objects.all()

	return render(request, 'taches/taches_list.html', {'taches':taches})







   

class TacheCreateView(PermissionRequiredMixin, BSModalCreateView):
    permission_required = 'taches.add_tache'
    template_name = 'taches/add_tache.html'
    form_class = AddTacheForm
    
    def form_valid(self , form):
        form.instance.project_id=Project
        return super(TacheCreateView , self ).form_valid(form)
    success_message = 'Success: task was created.'
    success_url = reverse_lazy('Projects:project_details')
    







