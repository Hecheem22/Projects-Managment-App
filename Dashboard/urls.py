from . import views
from django.urls import path

urlpatterns = [
  path('calendar/', views.CalendarView.as_view(), name='calendar'),
  path('' , views.project_dashboard , name='dashboard'),
  path('delete/<int:pk>', views.ProjectDeleteView.as_view(), name='delete_project'),
  path('update/<int:pk>', views.ProjectUpdateView.as_view(), name='update_project'),

  
]

