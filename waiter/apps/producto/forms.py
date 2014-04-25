from django import forms
from waiter.apps.producto.models import ESTADO_CHOICES, AreaProduccion, Categoria

class addProductForm(forms.Form):
	codigo = forms.CharField(widget=forms.TextInput())
	nombre = forms.CharField(widget=forms.TextInput())
	precio = forms.DecimalField(decimal_places=2)
	estado = forms.ChoiceField(required=True, widget=forms.Select(),choices=ESTADO_CHOICES)	
	categoria = forms.ModelChoiceField(queryset= Categoria.objects.all(), required=True)
	area_de_produccion = forms.ModelChoiceField(queryset= AreaProduccion.objects.all(), required=True)

	def clean(self):
		return self.cleaned_data

<<<<<<< HEAD
class addCategoria(forms.Form):
	categoria = forms.CharField(widget=forms.TextInput())
	def clean(self):
		return self.cleaned_data
    
class addAreaProduccion(forms.Form):
	area_de_produccion = forms.CharField(widget=forms.TextInput())
	def clean(self):
		return self.cleaned_data

		
=======
#class addIngredienteForm(forms.Form):
    
>>>>>>> b7636c699d5318ec8f5ae633eeec9fd52a3331e0
