from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
data = json.load(file)
all_language = []
all_legalities = []
all_color_identity = []
all_colors = []
all_keywords = []
all_set_acronym = []
all_set_name = []
all_set_type = []
all_rarity = []
all_type_line = []
all_artist = []
all_digital = []
all_manacost = []

for card in data:

	print(card['name'])
	try:	
		if card['lang'] not in all_language:
			all_language.append(card['language']) 
	except:
		pass
	try:		
		if card['legalities'] not in all_legalities:
			all_legalities.append(card['legalities']) 
	except:
		pass
	try:		
		if card['color_identity'] not in all_color_identity:
			all_color_identity.append(card['color_identity']) 
	except:
		pass
	try:		
		if card['colors'] not in all_colors:
			all_colors.append(card['colors']) 
	except:
		pass
	try:		
		if card['keywords'] not in all_keywords:
			all_keywords.append(card['keywords']) 
	except:
		pass
	try:		
		if card['set_acronym'] not in all_set_acronym:
			all_set_acronym.append(card['set_acronym']) 
	except:
		pass
	try:		
		if card['set_name'] not in all_set_name:
			all_set_name.append(card['set_name']) 
	except:
		pass
	try:		
		if card['set_type'] not in all_set_type:
			all_set_type.append(card['set_type']) 
	except:
		pass
	try:		
		if card['rarity'] not in all_rarity:
			all_rarity.append(card['rarity']) 
	except:
		pass
	try:		
		if card['type_line'] not in all_type_line:
			all_type_line.append(card['type_line']) 
	except:
		pass
	try:		
		if card['artist'] not in all_artist:
			all_artist.append(card['artist']) 
	except:
		pass
	try:		
		if card['digital'] not in all_digital:
			all_digital.append(card['digital']) 
	except:
		pass
	try:		
		if card['mana_cost'] not in all_manacost:
			all_manacost.append(card['mana_cost']) 
	except:
		pass
for x in all_language:
	Language.objects.create(language=x)
for x in all_legalities:
	legals = ''
	for key,value in x.items():
		if value =='legal':
			legals+=value+','
	Legalities.objects.create(legalities=legals)
for x in all_color_identity:
	Color_identity.objects.create(color_identity=x)
for x in all_colors:
	Colors.objects.create(colors=x)
for x in all_keywords:
	keys = ''.join(x)
	Keywords.objects.create(keywords=keys)
for x in all_set_acronym:
	Set_acronym.objects.create(set_acronym=x)
for x in all_set_name:
	Set_name.objects.create(set_name=x)
for x in all_set_type:
	Set_type.objects.create(set_type=x)
for x in all_rarity:
	Rarity.objects.create(rarity=x)
for x in all_type_line:
	Type_line.objects.create(type_line=x)
for x in all_artist:
	Artist.objects.create(artist=x)
for x in all_digital:
	Digital.objects.create(digital=x)
for x in all_manacost:
	Manacost.objects.create(manacost=x)