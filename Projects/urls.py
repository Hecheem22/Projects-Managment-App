from django.urls import path
from . import views
from Projects.views import SampleTable , DeleteProjectView , EditProjectView



urlpatterns = [
	path('create-project/', views.ProjectCreateView.as_view(), name='create_project'),
	path('projects-list/', SampleTable.as_view() , name='projects-List'),
	path('delete-project/<int:pk>/',DeleteProjectView.as_view(),name='delete_projeect'),
    path('edit-project/<int:pk>/',EditProjectView.as_view(),name='edit_project'),
	path('project-detail/<int:pk>/', views.ProjectDetailView.as_view(),name='project_details'),
	

   
   
]
