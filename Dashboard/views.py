from datetime import date, datetime ,  timedelta
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from Projects.models import Project
from .utils import Calendar
from Taches.models import Tache
from Projects.forms import AddProjectForm
from Taches.forms import AddTacheForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalUpdateView,BSModalDeleteView
)
from Projects.filters import ProjectFilter
from bootstrap_modal_forms.generic import BSModalReadView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required


class CalendarView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'projects.view_project'
    model = Project
    template_name = 'dashboard/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.GET.get('month'))
        d = get_date(self.request.GET.get('day', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'day=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'day=' + str(next_month.year) + '-' + str(next_month.month)
    return month

@login_required
@permission_required('projects.view_project', raise_exception=True)
def dashboard(request):
    projects = Project.objects.filter(ProjectManager=request.user)
    taches = Tache.objects.all()
    total_taches = taches.count()

    total_projects = projects.count()
    myFilter = ProjectFilter(request.GET , queryset=projects)
    projects = myFilter.qs 
    completed = projects.filter(Status='completed').count()
    uncompleted = projects.filter(Status='uncompleted').count()
    
    
    ToDo = taches.filter(Status='To Do').count()
    InProgress = taches.filter(Status='In Progress').count()
    Done = taches.filter(Status='Done').count()


    context = {'projects':projects, 'taches':taches,
    'total_projects':total_projects,'completed':completed,'To Do':ToDo,'In Progress':InProgress,'Done':Done,
    'uncompleted':uncompleted , 'total_taches':total_taches, 'myFilter':myFilter }

    return render(request, 'dashboard/dashboard.html', context)




class ProjectReadView(PermissionRequiredMixin, BSModalReadView):
    permission_required = 'projects.view_project'
    def get(self, request, pk):
        project=Project.objects.get(id=pk)
        context_data = {"taches":Tache.objects.filter(Project=project)}

        return render(request,'projects/read_project.html',context_data)


class TacheReadView(PermissionRequiredMixin, BSModalReadView):
    permission_required = 'taches.view_tache'
    model = Tache
    template_name = 'taches/tache_description.html'



class ProjectUpdateView(PermissionRequiredMixin, BSModalUpdateView):
    permission_required = 'projects.change_project'
    model = Project
    template_name = 'projects/update_project.html'
    form_class = AddProjectForm
    success_message = 'Success: Project was updated.'
    success_url = reverse_lazy('dashboard')

 



class ProjectDeleteView(PermissionRequiredMixin,BSModalDeleteView):
    permission_required = 'projects.delete_project'
    model = Project
    template_name = 'projects/project_delete.html'
    success_message = 'Success: Project was deleted.'
    success_url = reverse_lazy('dashboard')    




class TacheUpdateView(PermissionRequiredMixin,BSModalUpdateView):
    permission_required = 'taches.change_tache'
    model = Tache
    template_name = 'taches/update_tache.html'
    form_class = AddTacheForm
    success_message = 'Success: Tache was updated.'
    success_url = reverse_lazy('dashboard')

 



class TacheDeleteView(BSModalDeleteView):
    permission_required = 'taches.delete_tache'
    model = Tache
    template_name = 'taches/delete_tache.html'
    success_message = 'Success: Task was deleted.'
    success_url = reverse_lazy('dashboard')    








