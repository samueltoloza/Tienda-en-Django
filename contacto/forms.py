from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField()
    contenido = forms.CharField(widget=forms.Textarea, required=False)