from django.forms import ModelForm 
from .models import Players, Stats

class PlayerForm(ModelForm):
    class Meta:
        model = Players
        fields = ['name', 'bd']

class StatsForm(ModelForm):
    class Meta:
        model = Stats
        fields = ['goals_scored', 'starts']