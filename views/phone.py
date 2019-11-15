from django.shortcuts import render
def phone(request):
	return render(request, 'phone.html', {})

def qr_track(request):
	return render(request, 'cell_traceability.html', {})