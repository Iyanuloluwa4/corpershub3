from django import forms
from .models import CommonFlex
from django.forms import ModelForm


class FlexForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CommonFlex
        fields = [
            'video', 'picture', 'vibes'
        ]
        widgets = {
            'video': forms.ImageField(),
            'picture': forms.FileField(),
            'vibes': forms.Textarea(attrs={'style': 'width: 100%;'}),
        }