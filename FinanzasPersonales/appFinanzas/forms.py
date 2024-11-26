from django import forms
from .models import Transaccion

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['tipo', 'categoria', 'monto', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'monto': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }