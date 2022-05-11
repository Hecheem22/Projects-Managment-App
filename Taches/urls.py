from django.urls import path
from Taches import views




urlpatterns = [
	
	path('create-tache/', views.TacheCreateView.as_view(), name='create_tache'),
	path ('taches-list/', views.taches , name='Taches'),

]

