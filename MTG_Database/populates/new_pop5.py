import json
from mtg_app.models import *
with open("./newmtgdatabase.json") as file:
	card_data = json.load(file)

cmcs = Cmc.objects.all()
powers = Power.objects.all()
toughnesses = Toughness.objects.all()

cmc_dict = {}
power_dict = {}
toughness_dict = {}
for card in card_data:
	try:
		card_cmc = card['cmc']
		for cmc in cmcs:
			if card_cmc == cmc.cmc:
				cmc_dict[card['id']] = cmc
	except:
		pass
	try:
		card_power = card['power']
		for power in powers:
			if card_power == power.power:
				power_dict[card['id']] = power
	except:
		pass
	try:
		card_toughness = card['toughness']
		for toughness in toughnesses:
			if card_toughness == toughness.toughness:
				toughness_dict[card['id']] = toughness
	except:
		pass

cards = Card.objects.all()

for card in cards:
	try:
		card.power = power_dict[card.card_id]
		card.save()
	except:
		pass
	try:
		card.cmc = cmc_dict[card.card_id]
		card.save()
	except:
		pass
	try:
		card.toughness = toughness_dict[card.card_id]
		card.save()
	except:
		pass
	