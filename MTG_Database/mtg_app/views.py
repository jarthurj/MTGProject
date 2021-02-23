from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.core import serializers
from django.apps import apps
import json

def index(request):
	return render(request,'index.html')

def process_search(request):
	text_query = Card.objects.filter(name__icontains=request.POST['text_search'])

	colors = request.POST.getlist('colors')
	colors_str = "".join(colors)
	color = None
	cards_query = None
	if colors_str == "":
		cards_query = Card.objects.all()
	else:
		color = Colors.objects.filter(colors=colors_str)
		cards_query = color[0].cards.all()

	keywords_query = request.POST['keywords']
	keywords_cards = Card.objects.filter(card_keywords__icontains=keywords_query)
	# cards = keyword_object[0].cards.all()

	types_query = request.POST['types']
	types_cards = Card.objects.filter(card_type__icontains=types_query)

	cmc_query = request.POST['cmc']
	cmc_operator = request.POST['cmc_operator']
	cmc_objects = None
	cmc_cards = None
	if cmc_query != "":
		if cmc_operator == 'less_than': 
			cmc_objects = Cmc.objects.filter(cmc__lt=cmc_query)
		elif cmc_operator == 'greater_than':
			cmc_objects = Cmc.objects.filter(cmc__gt=cmc_query)
		elif cmc_operator == 'equal_to':
			cmc_objects = Cmc.objects.filter(cmc=cmc_query)
		elif cmc_operator == 'less_than_equal_to':
			cmc_objects = Cmc.objects.filter(cmc__lte=cmc_query)
		elif cmc_operator == 'greater_than_equal_to':
			cmc_objects = Cmc.objects.filter(cmc__gte=cmc_query)
		cmc_cards = cmc_objects[0].cards.all()
		for x in range(1,len(cmc_objects)):
			cmc_cards = cmc_cards.union(cmc_objects[x].cards.all())
	if cmc_cards:
		cards = text_query.intersection(cards_query, keywords_cards, types_cards,cmc_cards)
	else:
		cards = text_query.intersection(cards_query, keywords_cards, types_cards)
	data = serializers.serialize('json', list(cards), fields=('img_small_urls'))
	json_data = json.loads(data)
	request.session['return_cards'] = json_data
	request.session['colors']= colors_str
	return redirect('/results')

def display_results(request):

	cards = request.session['return_cards']
	context = {
		'cards':cards,
		'colors':request.session['colors']
	}
	return render(request, 'results.html', context)

def single_card_view(request, cardid):
	card = Card.objects.get(id=cardid)
	try:
		if request.session['userid']:
			user = User.objects.get(id=request.session['userid'])
			decks = user.decks.all()
	except:
		decks = None
	context = {
		'card':card,
		'decks':decks,
	}
	return render(request, 'single.html',context)

def login(request):
	if request.method == 'POST':
		user = User.objects.filter(email=request.POST['email'])
		if user[0].password == request.POST['password']:
			request.session['userid'] = user[0].id
			request.session['email'] = user[0].email
			return redirect('/')
		else:
			return redirect('/login')
	else:
		return render(request, 'login.html')

def logout(request):
	request.session.flush()
	return redirect('/')

def load_user_decks_page(request):
	user = User.objects.get(id=request.session['userid'])
	decks = user.decks.all()
	context = {
		'decks':decks
	}
	return render(request, 'user_decks.html', context)

def load_single_deck(request,deckid):
	deck = Deck.objects.get(id=deckid)
	context = {
		'deck':deck,
		'cards':deck.cards.all()
	}
	return render(request, 'single_deck.html',context)


def add_card_to_deck(request,cardid):
	deck = Deck.objects.get(id=request.POST['user_decks'])
	m1 = DeckMembership(card=Card.objects.get(id=cardid), deck=deck)
	m1.save()
	return redirect("/card/"+str(cardid))

def add_deck(request):
	new_deck = Deck.objects.create(name=request.POST['new_deck'], user=User.objects.get(id=request.session['userid']))
	return redirect("/decks")