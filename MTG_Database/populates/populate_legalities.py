from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
	card_data = json.load(file)

id_keyword_dict = {}

all_keywords = Keywords.objects.all()

for card in card_data:
	keywords = ""
	for k in card['keywords']:
			keywords += k + ','
	id_legal_dict[card['id']] = keywords[:-1]

# print(id_legal_dict)


# for x in id_legal_dict:
# 	id_legal_dict[x] = id_legal_dict[x][:-1]

print(id_legal_dict)

for card in Card.objects.all():
	for l in all_legals:
		if l.legalities == id_legal_dict[card.card_id]:
			card.legalities = l
			card.save()