from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from Accounts.models import User
 
admins, created = Group.objects.get_or_create(name ='admins')
ct = ContentType.objects.get_for_model(User)
permission = Permission.objects.get(codename ='add_user',
                                        name ='Can add user',
                                                content_type = ct)
admins.permissions.add(permission)