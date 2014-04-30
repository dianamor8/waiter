from django import forms
from waiter.apps.pedido.models import Pedido, ItemPedido

class addPedidoForm(forms.Form):
	codigo = forms.CharField(widget=forms.TextInput())
	estado_pedido = forms.ChoiceField(required=True, widget=forms.Select(),choices=ESTADO_CHOICES)		
	mesa = forms.IntegerField(widget=forms.TextInput())

	def clean(self):
		return self.cleaned_data

class addItemPedido(forms.Form):
	cantidad = forms.IntegerField(widget=forms.TextInput())
	# Aqui me falta lo del pedido, producto 
	#Estado del pedido 
    # TODO: Define form fields here
    

