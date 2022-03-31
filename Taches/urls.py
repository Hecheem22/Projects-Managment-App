from django.urls import path
from Taches import views




urlpatterns = [
	
	path('create-tache/', views.TacheCreateView.as_view(), name='create_tache'),
	path ('taches-list/', views.taches , name='Taches'),
	path ('users-taches/', views.UsersTaches , name='UsersTaches'),
	path ('add-user-tache/', views.UserTacheCreateView.as_view() , name='add_tache'),
]

