from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
	card_data = json.load(file)


digital_id_dict = {}

for card in card_data:

	digital_id_dict[card['id']] = card['digital']

digitals = Digital.objects.all()
cards = Card.objects.all()

for card in cards:
	for digit in digitals:
		if digit.digital == digital_id_dict[card.card_id]:
			card.digital = digit
			card.save()
	print(card.name, card.digital)

