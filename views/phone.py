from django.shortcuts import render
def phone(request):
	return render(request, 'phone.html', {})