from django.shortcuts import render
def phone(request):
	return render(request, 'phone.html', {})

def cell_traceability(request):
	return render(request, 'cell_traceability.html', {})