from django import forms

from .models import WeatherList

class WeatherForm(forms.ModelForm):

    class Meta:
        model = WeatherList
        fields = ('coment', 'zaryadka', 'today', 'smile',)