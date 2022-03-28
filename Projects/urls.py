from django.urls import path
from . import views
from Projects.views import SampleTable



urlpatterns = [
	path('create-project/', views.ProjectCreateView.as_view(), name='create_project'),
	path('projects-list/', SampleTable.as_view() , name='projects-List'),
	path('project-detail/<int:pk>/', views.ProjectDetailView.as_view(),name='project_details')
   
   
]
