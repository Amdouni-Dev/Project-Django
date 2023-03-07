from django import forms
from .models import Event
from .models import Person
class EventForm(forms.Form):
    title=forms.CharField(label="Tapez le titre de l'événement",max_length=9, widget=forms.TextInput(attrs={'class':'form-control'}))# widget bech naamel biha personnalistaion lel champs input 
    description=forms.CharField(label="Tapez la description de l'événement",widget=forms.Textarea(attrs={'class':'form-control'}))# widget bech naamel biha personnalistaion lel champs
    image=forms.ImageField(label='choisissez une image',required=False)
    nbrParticipants=forms.IntegerField(label="Tapez le nombre de participants",min_value=0,max_value=10)
    dateEvent=forms.DateField(label="Tapez la date de l'événement" ,widget=forms.DateInput(
        attrs={'type':'date'}
    ) )
    organizer=forms.ModelChoiceField(queryset=Person.objects.all(),label="Choisir un organizer")

    
class EventModelForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=['title','description','image','nbrParticipants','dateEvent','organizer']
        exclude=('state',)
    dateEvent=forms.DateField(
        label="Tapez la date de l'événement",widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control  date-input'}))    
                          
    organizer=forms.ModelChoiceField(queryset=Person.objects.all(),label="Choisir un organizer")
    
                       
class DeleteEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = []


class EventModelFormPArticipation(forms.ModelForm):
    class Meta:
        model=Event
        fields=['participations']
        #exclude=('state',)       