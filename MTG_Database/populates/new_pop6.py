import json
from mtg_app.models import *
with open("./newmtgdatabase.json") as file:
	card_data = json.load(file)

cards =Card.objects.all()

rares = Rarity.objects.all()
rare_dict = {}
for card in card_data:
	for rare in rares:
		if rare.rarity==card['rarity']:
			rare_dict[card['id']] = rare

for card in cards:
	card.rarity = rare_dict[card.card_id]
	card.save()
