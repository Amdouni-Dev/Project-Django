from django.contrib import admin
from .models import Person # wila hakka from .models import Event khter deja f west l dosier events
from django.utils.html import mark_safe
from django.utils.html import format_html
from django.contrib import messages

# Register your models here.
# admin.site.register(Person)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('cin', 'email', 'username')
    list_filter = ('cin', 'email', 'username')
    ordering = ('cin', 'email', 'username')
    search_fields=['cin']
    fieldsets =[('Informations personnelles', { 'fields' : ('cin','username','email') } )]
    
    def accept_events(self,request,queryset):
        rows_updated=queryset.update(state=True)
        if rows_updated ==1:
            msg="1 event"
        else:
            msg=f"{rows_updated} events"
        messages.success(request,message= "%s successfully accepted " %msg)

# refus 
    
    
    # readonly_fields = ('image_tag',)

    # def get_fields(self, request, obj=None):
    #     fields = super().get_fields(request, obj)
    #     fields += ('image_tag',)
    #     return fields
    # def profile_pic(self, obj):
    #     return mark_safe(f'<img src="/media/{obj.image}"width="150" height="150" />')


# Register your models here.
