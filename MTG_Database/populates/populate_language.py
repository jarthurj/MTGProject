from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
	card_data = json.load(file)

id_lang_dict = {}

for card in card_data:
	id_lang_dict[card['id']] = card['lang']

langs = list(Language.objects.all())
all_cards = Card.objects.all()

for card in all_cards:
	card_lang = id_lang_dict[card.card_id]
	for l in langs:
		if l.language == card_lang:
			card.language = l
			card.save()
			print(type(l))
