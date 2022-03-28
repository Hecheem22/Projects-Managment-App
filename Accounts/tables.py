from xml.dom.minidom import Attr
import django_tables2 as tables
from Accounts.models import User

class UserTable(tables.Table):
  
    
    
    
    class Meta:
        model = User
        attrs = {'id': 'users_table',
        'class' : 'table table-sm table-responsive-sm table-hover text-nowrap table-striped table-bordered'}
        template_name = "django_tables2/bootstrap.html"
        fields = ( "first_name", "last_name" , "email" , "Type" )