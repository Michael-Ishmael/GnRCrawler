__author__ = 'michaeli'

from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


