from django import forms


class ArtForm(forms.Form):
    text = forms.CharField(label="", max_length=20, required=True)
