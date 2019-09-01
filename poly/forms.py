from django import forms

from polygen.models import PolyPoints

class PostForm(forms.ModelForm):

    class Meta:
        model = PolyPoints
        fields=[
            '_lat',
            '_long',
        ]