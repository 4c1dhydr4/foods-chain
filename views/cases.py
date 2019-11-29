from django.shortcuts import render
from datetime import datetime

def salida_almacen(request):
	now = datetime.today()
	tomo = "{}/{}/{} {}:{}".format(
			now.day + 1,
			now.month,
			now.year,
			now.hour + 2,
			now.minute + 5,
		)
	return render(request, 'case/salida_almacen.html', {'now':now, 'tomo':tomo})

def llegada_importador(request):
	now = datetime.today()
	tomo = "{}/{}/{} {}:{}".format(
			now.day + 1,
			now.month,
			now.year,
			now.hour + 2,
			now.minute + 5,
		)
	return render(request, 'case/llegada_importador.html', {'now':now, 'tomo':tomo})

