from django import forms


class ArtForm(forms.Form):
    text = forms.CharField(
        label="",
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter something:'}
        )
    )
