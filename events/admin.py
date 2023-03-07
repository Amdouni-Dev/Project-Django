from django.contrib import admin
from events.models import Event # wila hakka from .models import Event khter deja f west l dosier events
from events.models import Participation
from datetime import datetime;
# Register your models here.
class ParticipantFilter(admin.SimpleListFilter):
    title="Nbr Participant"
    parameter_name = 'nbrParticipants'
    def lookups(self, request, model_admin):
        return ( ('0',("No Participant")),('more',('more participant')) )
    def queryset(self, request, queryset):
        if self.value() == 'more':
            return queryset.filter(nbrParticipants__gt=0)

        if self.value() == '0':
            return queryset.filter(nbrParticipants__exact=0)
            
# class DateFilter(admin.SimpleListFilter):
#     title="Date"
#     parameter_name="evt_date"
#     def lookups(self, request, model_admin):
#         return ( ('Past events',("Past events")),('Upcoming event',("Upcoming event")),("Today Event"('Today Event' )))
#     def queryset(self, request, queryset):
#         if self.value() == 'Past events':
#             return queryset.filter(dateEvent__lt=datetime.today())
#         if self.value() == 'Upcoming event':
#             return queryset.filter(dateEvent__gt=datetime.today())
            
#         if self.value() == 'Today Event':
#             return queryset.filter(dateEvent__exact=datetime.today())
               


@admin.register(Event)
class eventadmin(admin.ModelAdmin):
    #pass # l class fergha
    list_display=('title','state','category','event_participant','dateEvent') # (les attributs eli bech ybenouli f tableau)tableau fih hedhom meaach tjini form d'ajout 
    list_filter=('title','state','category',ParticipantFilter)#,DateFilter)

    #ordering=('title','state','category') # ordre ==>Tri 
    ordering=('-title',) #ordre decroissant bel alphabet 
    search_fields=['title','category']
    list_per_page=2 #pagination
    
# admin.site.register(Event,eventadmin)
    #hdhy function bech nehseb 
    def event_participant(self,obj):
        count=obj.participations.count()
        return count
@admin.register(Participation)
class participationAdmin(admin.ModelAdmin):
    list_display=('participationDate','event','person')
    list_filter=('participationDate','event','person')
    ordering=('participationDate','event','person')
    search_fields=['participationDate']



#admin.site.register(Participation)


#Personnalistaion
