from django.shortcuts import redirect
from Taches.models import Tache
from Taches.forms import AddTacheForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from bootstrap_modal_forms.generic import BSModalCreateView 


class TacheCreateView(BSModalCreateView):
    template_name = 'taches/add_tache.html'
    form_class = AddTacheForm
    success_message = 'Success: tache was created.'
    success_url = reverse_lazy('TachesList')





class DeleteTacheView(DeleteView):
    model = Tache
    success_url = reverse_lazy('TachesList')
    def get(self, *args, **kwargs):
         return self.post(*args, **kwargs)


class UpdateTacheView(UpdateView):

    model = Tache
    fields = ["Name", "Description" , "StartDate" , "EndDate" , "Status"  ]
    template_name = 'taches/update_tache.html'
    context_object_name = 'tache'

    def form_valid(self, form):
        projet = form.save(commit=False)
        projet.save()
        return redirect('TachesList')


