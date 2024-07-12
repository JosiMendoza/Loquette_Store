from  django.forms import ModelForm, DateField,DateInput
from .models import Cliente


class RegistroForm(ModelForm):
    class Meta:
        model = Cliente
        fields =['rut','nombres','apellidos','email','direccion']
