import django_tables2 as tables
from .models import Project





class ProjectTable(tables.Table):
 Details = tables.TemplateColumn('<a href="{{ record.get_absolute_url }}" class="btn btn-info"><i class="fa fa-eye"></i></a>', orderable=False  , attrs={"tf": {"class": "my-class" ,  }})  

   
 class Meta:
        model = Project
        attrs = {'id': 'projects_table',
        'class' : 'table table-sm table-responsive-sm table-hover text-nowrap table-striped table-bordered'}
        template_name = "django_tables2/bootstrap.html"
        fields = ("id" , "Title", "Description" , "StartDate" , "EndDate" , "ProjectManager"   )
        sequence = ('id','Title', 'Description' , 'StartDate' , 'EndDate' , 'ProjectManager'    )
        
        
