import django_tables2 as tables
from Accounts.models import User

class UserTable(tables.Table):
  
 Edit = tables.TemplateColumn('<a href="{{ record.get_edit_user_url }}" class="btn btn-info"><i class="fa fa-edit"></i></a>', orderable=False)
 Delete = tables.TemplateColumn('<a href="{{ record.get_delete_user_url }}" class="btn btn-info"><i class="fa fa-trash"></i></a>', orderable=False)    
    
    
 class Meta:
        model = User
        attrs = {'id': 'users-table',
        'class' : 'table table-sm table-responsive-sm table-hover text-nowrap table-striped table-bordered'}

        fields = ( "first_name", "last_name" , "email" , "Type" )








    