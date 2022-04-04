from datetime import date, datetime ,  timedelta
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from Projects.models import Project
from .utils import Calendar
from Taches.models import Tache
from Projects.forms import AddProjectForm
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalUpdateView,BSModalDeleteView
)
from Projects.filters import ProjectFilter





class CalendarView(generic.ListView):
    model = Project
    template_name = 'dashboard/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def project_dashboard(request):
    projects = Project.objects.filter(ProjectManager=request.user)
    total_projects = projects.count()
    myFilter = ProjectFilter(request.GET , queryset=projects)
    projects = myFilter.qs 
    completed = projects.filter(Status='completed').count()
    uncompleted = projects.filter(Status='uncompleted').count()


    context = {'projects':projects, 
    'total_projects':total_projects,'completed':completed,
    'uncompleted':uncompleted , 'myFilter':myFilter }

    return render(request, 'dashboard/dashboard.html', context)



class ProjectUpdateView(BSModalUpdateView):
    model = Project
    template_name = 'projects/update_project.html'
    form_class = AddProjectForm
    success_message = 'Success: Project was updated.'
    success_url = reverse_lazy('dashboard')

 



class ProjectDeleteView(BSModalDeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_message = 'Success: Project was deleted.'
    success_url = reverse_lazy('dashboard')    




def Taches(request):
	taches = Tache.objects.all()

	return render(request, 'dashboard/taches_table.html', {'taches':taches})

