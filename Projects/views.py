from django.shortcuts import render , redirect
from Projects.forms import AddProjectForm
from .tables import ProjectTable
from .models import Project
from django.views.generic.base import View
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView 
from Taches.models import Tache
from django.views.generic import DeleteView , UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin


class ProjectCreateView(PermissionRequiredMixin,BSModalCreateView):
    permission_required = 'projects.add_project'
    template_name = 'projects/add_project.html'
    form_class = AddProjectForm
    success_message = 'Success: project was created.'
    success_url = reverse_lazy('projects-List')
   
class DeleteProjectView(PermissionRequiredMixin,DeleteView):
    permission_required = 'projects.delete_project'
    model = Project
    success_url = reverse_lazy('projects-List')
    def get(self, *args, **kwargs):
         return self.post(*args, **kwargs)


class EditProjectView(PermissionRequiredMixin,UpdateView):
    permission_required = 'projects.change_project'
    model = Project
    fields = [ "Title", "Description" , "StartDate" , "EndDate" , "ProjectManager" , "Status"   ]
    template_name = 'projects/edit_project.html'
    context_object_name = 'projet'

    def form_valid(self, form):
        projet = form.save(commit=False)
        projet.save()
        return redirect('projects-List')


class ProjectDetailView(PermissionRequiredMixin,View):
    permission_required = 'taches.view_tache'
    def get(self, request, pk):
        project=Project.objects.get(id=pk)
        context_data = {"taches":Tache.objects.filter(Project=project)}

        return render(request,'projects/project_details.html',context_data)




class SampleTable(PermissionRequiredMixin,View):
 permission_required = 'projects.view_project'
 def get(self,request):
        queryset = Project.objects.filter(ProjectManager=request.user)
        project_table = ProjectTable(queryset)
       
        context = {'view_project':project_table }
        return render(request, 'projects/projects_list.html', context)
        

        
