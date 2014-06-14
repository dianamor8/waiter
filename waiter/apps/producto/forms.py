from django import forms
from django.forms import ModelForm
from waiter.apps.producto.models import ESTADO_CHOICES, AreaProduccion, Categoria

class addProductForm(forms.Form):
	codigo = forms.CharField(widget=forms.TextInput())
	nombre = forms.CharField(widget=forms.TextInput())
	precio = forms.DecimalField(decimal_places=2)
	estado = forms.ChoiceField(required=True, widget=forms.Select(),choices=ESTADO_CHOICES)	
	categoria = forms.ModelChoiceField(queryset= Categoria.objects.all(), required=True)
	area_de_produccion = forms.ModelChoiceField(queryset= AreaProduccion.objects.all(), required=True)
	imagen = forms.ImageField(required=False)
	def clean(self):
		return self.cleaned_data

class addCategoriaForm(ModelForm):	
	class Meta:
		model = Categoria
		# fields = ("nombre")
	
class addAreaProduccion(forms.Form):
	area_de_produccion = forms.CharField(widget=forms.TextInput())
	def clean(self):
		return self.cleaned_data