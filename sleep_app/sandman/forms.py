from django import forms
from sandman.models import Help

class HelpForm(forms.ModelForm):
    name = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256, required=True)
    subject = forms.CharField(max_length=256)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Help

