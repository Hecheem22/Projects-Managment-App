from . import views
from django.urls import path

urlpatterns = [
  path('calendar/', views.CalendarView.as_view(), name='calendar'),
  path('calendar/<month>', views.CalendarView.as_view(), name='calendar_month'),
  path('' , views.dashboard , name='dashboard'),
  path('delete/<int:pk>', views.ProjectDeleteView.as_view(), name='delete_project'),
  path('update/<int:pk>', views.ProjectUpdateView.as_view(), name='update_project'),
  path('delete-tache/<int:pk>', views.TacheDeleteView.as_view(), name='delete_tache'),
  path('update-tache/<int:pk>', views.TacheUpdateView.as_view(), name='update_tache'),
  path('read-project/<int:pk>', views.ProjectReadView.as_view(), name='read_project'),
  path('read-tache/<int:pk>', views.TacheReadView.as_view(), name='read_tache'),
]

