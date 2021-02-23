from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
	card_data = json.load(file)

def bisect(word, word_list):
	i = len(word_list) // 2

	if len(word_list) == 0:
		return False
	if str(word_list[i].keywords) == word:
		return word_list[i]
	if word < str(word_list[i].keywords):
		return bisect(word, word_list[:i])
	else:
		return bisect(word, word_list[i:])
id_keyword_dict = {}

all_keywords = list(Keywords.objects.all())
# all_keywords.sort()
for card in card_data:
	keywords = ""
	key_list = card['keywords']
	key_list.sort()
	for k in key_list:
			keywords += k + ','
	id_keyword_dict[card['id']] = keywords[:-1]

# print(id_legal_dict)


# for x in id_legal_dict:
# 	id_legal_dict[x] = id_legal_dict[x][:-1]

# print(id_legal_dict)

for card in Card.objects.all():
	card.keywords = bisect(id_keyword_dict[card.card_id],all_keywords)
	card.save()
	print(card.name, card.keywords)
	