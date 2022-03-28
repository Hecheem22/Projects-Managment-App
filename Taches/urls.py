from django.urls import path
from Taches import views
from Taches.views import DeleteTacheView , UpdateTacheView



urlpatterns = [
	
	path('create-tache/', views.TacheCreateView.as_view(), name='create_tache'),
	path('delete-tache/<int:pk>/',DeleteTacheView.as_view(),name='delete_tache'),
    path('update-tache/<int:pk>/',UpdateTacheView.as_view(),name='update_tache'),
]
