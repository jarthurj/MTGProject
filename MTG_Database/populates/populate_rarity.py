from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
	card_data = json.load(file)


id_rare = {}

for card in card_data:
	id_rare[card['id']] = card['rarity']

for card in Card.objects.all():
	for rare in Rarity.objects.all():
		if rare.rarity == id_rare[card.card_id]:
			card.rarity = rare
			card.save()