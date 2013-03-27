from django.contrib import admin
from models import *

admin.site.register(Person)
admin.site.register(Link)
admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(Edition)
admin.site.register(Role)

class PRAdmin(admin.ModelAdmin):
    list_display = ('person', 'edition', 'role')

admin.site.register(PersonRole, PRAdmin)
