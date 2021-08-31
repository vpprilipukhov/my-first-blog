from django.forms import ModelForm
from .models import Bd

class Bbform(ModelForm):
    class Meta:
        model = Bd
        fields = ('title', 'content','price','rubric')


