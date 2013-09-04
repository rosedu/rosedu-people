from django.contrib import admin
from models import *

admin.site.register(Link)
admin.site.register(Organization)
admin.site.register(Role)

class PRAdmin(admin.ModelAdmin):
    list_display = ('person', 'edition', 'role')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'is_active', 'is_staff')

class PersonRoleInlineAdmin(admin.StackedInline):
    model = PersonRole
    extra = 0

class EditionAdmin(admin.ModelAdmin):
    list_display = ('project', 'name')
    inlines = [PersonRoleInlineAdmin, ]

class EditionInlineAdmin(admin.StackedInline):
    model = Edition
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    inlines = [EditionInlineAdmin, ]

admin.site.register(PersonRole, PRAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Edition, EditionAdmin)
