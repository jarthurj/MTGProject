from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
	card_data = json.load(file)


color_id_dict = {}

for card in card_data:
	color_str = ""
	try:
		for color in card['colors']:
			color_str += str(color)
	except:
		pass
	color_id_dict[card['id']] = color_str

colors = Colors.objects.all()
cards = Card.objects.all()

for card in cards:
	for color in colors:
		if color.colors == color_id_dict[card.card_id]:
			card.colors = color
			card.save()
	print(card.name, card.colors)

