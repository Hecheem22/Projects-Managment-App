from django.shortcuts import render
from django.shortcuts import render
from Projects.forms import AddProjectForm
from .tables import ProjectTable
from .models import Project
from django.views.generic.base import View
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView 
from Taches.models import Tache

class ProjectCreateView(BSModalCreateView):
    template_name = 'projects/add_project.html'
    form_class = AddProjectForm
    success_message = 'Success: project was created.'
    success_url = reverse_lazy('projects-List')
   

class ProjectDetailView(View):

    def get(self, request, pk):

        context_data = {"tache":Tache.objects.get(id=pk)}

        return render(request,'taches/taches_list.html',context_data)

class SampleTable(View):
 def get(self,request):
        queryset = Project.objects.filter(ProjectManager=request.user)
        project_table = ProjectTable(queryset)
        context = {'view_project':project_table}
        return render(request, 'projects/projects_list.html', context)
        
