from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

#Vista con render_to_response
#def index_view(request):
#	return render_to_response('home/index.html', context_instance = RequestContext(request))

#Vista con render
def index_view(request):
	return render(request, 'home/index.html')

def about_view(request):
	mensaje = "Este es mi mensaje"
	ctx = {'msg':mensaje}
	return render(request, 'home/about.html',ctx)