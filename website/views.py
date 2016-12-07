from django.shortcuts import render

# Create your views here.

def inicio(request):
	# query = Negocio.objects.all()
	# context = {
	# 	"lista_negocios":query
	# }
	return render(request, 'inicio.html')