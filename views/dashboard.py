from django.shortcuts import render
from views.choices import (departments, citys, products, companies, stats)
import random
import hashlib

def index(request):
	context = {}
	return render(request, 'index.html', context)

def tacks(request):
	tracks = []
	for x in range(0,100):
		tracks.append({
			'company':random.choice(companies),
			'status':random.choice(stats),
			'origin': random.choice(departments),
			'destination': random.choice(citys),
			'product': random.choice(products),
			'quantity': random.randint(100,1200),
			'lote': random.randint(1,10),
			'lote': random.randint(1,10),
			'hash': hashlib.md5(str(random.randint(1,150000)).encode()).hexdigest,
			'date': '{}/{}/2019'.format(random.randint(1,30),random.randint(9,10)),
			'blocks': random.randint(1,20),
		})
	context = {
		'tracks':tracks,
	}
	return render(request, 'tracks.html', context)
