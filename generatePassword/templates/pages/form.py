from django import forms


class PasswordGeneratorForm(forms.Form):
    email = forms.EmailField(label="Email")
    app_name = forms.CharField(label="App/Website Name")
