import json
with open("./newmtgdatabase.json") as file:
	card_data = json.load(file)


colors_list = []

for card in card_data:
	print(card['name'])
	try:
		colors_str = "".join(card['colors'])
		if colors_str not in colors_list:
			colors_list.append(colors_str)
	except:
		pass
for color in colors_list:
	Colors.objects.create(colors=color)