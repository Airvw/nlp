from django import forms

from .models import UploadFile

class UplaodFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('title', 'file')