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
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from bootstrap_modal_forms.generic import (BSModalUpdateView,BSModalDeleteView
)






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
	projects = Project.objects.all()
	total_projects = projects.count()
	Termine = projects.filter(Status='Terminé').count()
	En_cours = projects.filter(Status='En cours').count()
   

	context = {'projects':projects, 
    'total_projects':total_projects,'Terminé':Termine,
	'En cours':En_cours }

	return render(request, 'dashboard/dashboard.html', context)


def tache_dashboard(request):
	taches = Tache.objects.all()
	total_taches = taches.count()
	Complete = taches.filter(Status='Complete').count()
	Incomplete = taches.filter(Status='Incomplete').count()
    

	context = {'taches':taches, 
    'total_taches':total_taches,'Complete':Complete,
	'Incomplete':Incomplete }

	return render(request, 'dashboard/taches_status.html', context)


class ProjectUpdateView(BSModalUpdateView):
    model = Project
    template_name = 'projects/update_proj.html'
    form_class = AddProjectForm
    success_message = 'Success: Project was updated.'
    success_url = reverse_lazy('dashboard')

 



class ProjectDeleteView(BSModalDeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_message = 'Success: Project was deleted.'
    success_url = reverse_lazy('dashboard')    






