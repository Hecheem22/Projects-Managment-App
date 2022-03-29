from django.urls import path
from Accounts.views import UserListView , DeleteUserView , EditUserView
from . import views

urlpatterns = [
 
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('create-user/', views.UserCreateView.as_view(), name='create_user'),
    path('delete-user/<int:pk>/',DeleteUserView.as_view(),name='delete_user'),
    path('edit-user/<int:pk>/',EditUserView.as_view(),name='edit_user'),
    path('users-list/', UserListView.as_view() , name='userslist'),
    

]