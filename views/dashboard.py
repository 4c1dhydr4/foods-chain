from django.shortcuts import render
from views.choices import (departments, citys, products, companies, stats, proces)
import random as r
import hashlib


def get_cards(blocks):
	block_list = []
	for x in range(0,blocks):
		if x == 0:
			origin = r.choice(departments) + ', PE'
			date_in = (r.randint(1,15),r.randint(9,10))
		date_out = (date_in[0]+2,date_in[1])
		destination = r.choice(citys)
		card = {
			'origin': origin,
			'destination': destination[1],
			'country': destination[0],
			'date_in': '{}/{}/2019'.format(date_in[0],date_in[1]),
			'date_out': '{}/{}/2019'.format(date_out[0],date_out[1]),
			'stat': proces[x],
			'public_k': hashlib.md5(str(r.randint(1,150000)).encode()).hexdigest,
			'private_k': hashlib.md5(str(r.randint(1,150000)).encode()).hexdigest,
			'id': r.randint(1,20)
		}
		origin = destination[1]
		date_in = (date_out[0]+1,date_out[1])
		block_list.append(card)
	return block_list

def get_blockchain():
	blocks = r.randint(1,4)
	return {
		'company':r.choice(companies),
		'status':r.choice(stats),
		'origin': r.choice(departments),
		'destination': r.choice(citys),
		'product': r.choice(products),
		'quantity': r.randint(100,1200),
		'lote': r.randint(1,10),
		'hash': hashlib.md5(str(r.randint(1,150000)).encode()).hexdigest,
		'date': '{}/{}/2019'.format(r.randint(1,30),r.randint(9,10)),
		'blocks': blocks,
		'block_cards': get_cards(blocks)
	}

def index(request):
	context = {}
	return render(request, 'index.html', context)

def tacks(request):
	tracks = []
	for x in range(0,100):
		tracks.append(get_blockchain())
	context = {
		'tracks':tracks,
	}
	return render(request, 'tracks.html', context)

def blockchain_card(request):
	return render(request, 'blockchain_card.html', get_blockchain())

def traceability(request):
	context = {
		'':''
	}
	return render(request, 'traceability.html', context)
