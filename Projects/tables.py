import django_tables2 as tables
from .models import Project





class ProjectTable(tables.Table):

       Edit = tables.TemplateColumn('<a href="{{ record.get_edit_project_url }}" class="btn btn-info"><i class="fa fa-edit"></i></a>', orderable=False)
       Delete = tables.TemplateColumn('<a href="{{ record.get_delete_projeect_url }}" class="btn btn-info"><i class="fa fa-trash"></i></a>', orderable=False)    
       Details = tables.TemplateColumn('<a href="{{ record.get_absolute_url }}" class="btn btn-info"><i class="fa fa-eye"></i></a>', orderable=False  )  
       
       class Meta:
        model = Project
        attrs = {'id': 'projects-table',
        'class' : 'table table-striped table-hover' , }
        fields = ( "Title", "Description" , "StartDate" , "EndDate" , "ProjectManager" , "Status"   )
       
        
        
        

        
        
