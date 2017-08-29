from django.shortcuts import render


# Create your views here.
def estadisticas(request):
    return render(request, 'pagina/estadisticas.html', {})


def index(request):
    return render(request, 'pagina/index.html', {})


def reglas(request):
    return render(request, 'pagina/reglas.html', {})

