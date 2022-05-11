from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse_lazy
from .models import *
from Accounts.forms import AddUserForm
from .tables import UserTable
from django_tables2 import SingleTableView
from bootstrap_modal_forms.generic import BSModalCreateView
from django.views.generic import DeleteView , UpdateView
from .forms import LoginForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('projects.view_project', raise_exception=True)
@permission_required('taches.view_tache', raise_exception=True)
def index(request):
    return render(request, 'accounts/dashboard.html')


def loginPage(request):
	
			form = LoginForm()

			
			if request.method == "POST":
				form=LoginForm(request.POST)

				if form.is_valid():
					username = form.cleaned_data.get("username")
					password = form.cleaned_data.get("password")
					form.save()
					
					user = authenticate(username=username, password=password)
					if user is not None:
						login(request, user)
						return redirect('')
					
			return render(request, "accounts/login.html", {"form": form})





def logoutUser(request):
	logout(request)
	return redirect('login')


class UserCreateView(PermissionRequiredMixin,BSModalCreateView):
    permission_required = 'accounts.add_user'
    template_name = 'accounts/adduser.html'
    form_class = AddUserForm
    success_message = 'Success: user was created.'
    success_url = reverse_lazy('userslist')

class DeleteUserView(PermissionRequiredMixin,DeleteView):
    permission_required = 'accounts.delete_user'
    model = User
    success_url = reverse_lazy('userslist')
    def get(self, *args, **kwargs):
         return self.post(*args, **kwargs)


class EditUserView(PermissionRequiredMixin,UpdateView):
    permission_required = 'accounts.change_user'
    model = User
    fields = ["first_name", "last_name" , "email" , 'Type' ]
    template_name = 'accounts/edit_user.html'
    context_object_name = 'projet'

    def form_valid(self, form):
        projet = form.save(commit=False)
        projet.save()
        return redirect('userslist')


class UserListView(PermissionRequiredMixin,SingleTableView):
    permission_required = 'accounts.view_user'
    model = User
    table_class = UserTable
    template_name = 'accounts/users_list.html'
	


