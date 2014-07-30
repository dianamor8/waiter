from django.shortcuts import render
from waiter.apps.conexiones.models import Product_external_view
from waiter.settings import LOGIN_URL, LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required
from waiter.apps.conexiones.forms import addConexionDataBaseForm
# Create your views here.

@login_required(login_url=LOGIN_URL)
def view_configuration_productos(request):
	productos = Product_external_view.objects.all()	
	if request.method=='GET':		
		form = addConexionDataBaseForm()		
		ctx = {'productos':productos, 'sidebar':'administracion', 'form_conexion':form}
	else:	
		ctx = {'productos':productos, 'sidebar':'administracion'}
	return render(request, 'home/panel_administracion/configurations.html', ctx)
