from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
	card_data = json.load(file)


mana_id_dict = {}

for card in card_data:
	mana_str = ""
	try:
		mana_str = card['mana_cost']
	except:
		pass
	mana_id_dict[card['id']] = mana_str

manacost = Manacost.objects.all()
cards = Card.objects.all()

for card in cards:
	for mana in manacost:
		if mana.manacost == mana_id_dict[card.card_id]:
			card.manacost = mana
			card.save()
	print(card.name, card.manacost)

