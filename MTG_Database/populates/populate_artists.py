# this is to populate the database

from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
	card_data = json.load(file)
# data is a list filled with dicationaries
# each dictionary in the list is card object
def bisect(word, word_list):
	i = len(word_list) // 2

	if len(word_list) == 0:
		return False
	if str(word_list[i].artist) == word:
		return word_list[i]
	if word < str(word_list[i].artist):
		return bisect(word, word_list[:i])
	else:
		return bisect(word, word_list[i:])

artists = Artist.objects.all()

art_id_dict = {}

for card in card_data:
	art_id_dict[card['id']] = card['artist']
card_list = Card.objects.all()

for card in card_list:
	card.artist = bisect(art_id_dict[card.card_id], list(artists))
	card.save()
	print(card.name, card.artist)