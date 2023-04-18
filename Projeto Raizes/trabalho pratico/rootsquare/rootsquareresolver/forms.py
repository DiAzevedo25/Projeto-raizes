from django import forms

class Form(forms.Form):
    a = forms.FloatField(label='a', required=True)
    b = forms.FloatField(label='b', required=True)
    c = forms.FloatField(label='c', required=True)

#floatfield = campos numericos decimal