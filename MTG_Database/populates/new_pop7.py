import json
from mtg_app.models import *
with open("./newmtgdatabase.json") as file:
	card_data = json.load(file)

cards = Card.objects.all()
colors = Colors.objects.all()
color_dict = {}

for card in card_data:
	color_str = ""
	try:
		for color in card['colors']:
			color_str += color
		for color in colors:
			if color.colors == color_str:
				color_dict[card['id']] = color
	except:
		pass

for card in cards:
	try:
		card.colors = color_dict[card.card_id]
		card.save()
	except:
		pass
