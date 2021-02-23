import json
from mtg_app.models import *
with open("./newmtgdatabase.json") as file:
	card_data = json.load(file)

cmc_list = []
power_list = []
toughness_list = []


for card in card_data:
	try:
		if card['toughness'] not in toughness_list:
			toughness_list.append(card['toughness'])
	except:
		pass
	try:
		if card['power'] not in power_list:
			power_list.append(card['power'])
	except:
		pass
	try:
		if float(card['cmc']) not in cmc_list:
			cmc_list.append(float(card['cmc']))
	except:
		pass


for cmc in cmc_list:
	Cmc.objects.create(cmc=cmc)

for power in power_list:
	Power.objects.create(power=power)
for toughness in toughness_list:
	Toughness.objects.create(toughness=toughness)