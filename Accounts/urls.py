from django.urls import path
from Accounts.views import UserListView


from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('create-user/', views.UserCreateView.as_view(), name='create_user'),
    path('users-list/', UserListView.as_view() , name='userslist'),
    

]