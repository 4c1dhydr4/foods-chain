from django.shortcuts import render
from datetime import datetime

def salida_almacen(request):
	now = datetime.today()
	return render(request, 'case/salida_almacen.html', {'now':now})