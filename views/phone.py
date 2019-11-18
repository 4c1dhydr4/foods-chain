from django.shortcuts import render
def phone(request):
	return render(request, 'phone.html', {})

def qr_track(request, opt=0):
	context = {}
	if opt == 0:
		context['empresa'] = True
	if opt == 1:
		context['empresa'] = False
	return render(request, 'cell_traceability.html', context)

def company_login(request):
	return render(request, 'company_login.html', {})

def client_select(request, opt=0):
	return render(request, 'client_select.html', {})

	