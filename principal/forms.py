from django import forms

from .models import Empleados

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'