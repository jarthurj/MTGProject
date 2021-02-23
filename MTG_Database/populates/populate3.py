from mtg_app.models import *
import json

with open("newmtgdatabase.json") as file:
	card_data = json.load(file)

for card in card_data:
	try:
		name = card['name']
	except:
		name = None
	try:
		card_id = card['id']
	except:
		card_id = None
	try:
		cmc = card['cmc']
	except:
		cmc = None
	try:
		power = card['power']
	except:
		power = None
	try:
		toughness = card['toughness']
	except:
		toughness = None
	try:
		flavor_text = card['flavor_text']
	except:
		flavor_text = None
	try:
		oracle_text = card['oracle_text']
	except:
		oracle_text = None
	try:
		img_art_crop_url = card['image_uris']['art_crop']
	except:
		img_art_crop_url = None
	try:
		img_border_crop_url = card['image_uris']['border_crop']
	except:
		img_border_crop_url = None
	try:
		img_large_url = card['image_uris']['large']
	except:
		img_large_url = None
	try:
		img_png_url = card['image_uris']['png']
	except:
		img_png_url = None
	try:
		img_small_url = card['image_uris']['small']
	except:
		img_small_url = None

	Card.objects.create(
		name = name,
		card_id = card_id,
		cmc = cmc,
		power = power,
		toughness = toughness,
		flavor_text = flavor_text,
		oracle_text = oracle_text,
		img_art_crop_url = img_art_crop_url,
		img_border_crop_url = img_border_crop_url,
		img_large_url = img_large_url,
		img_png_url = img_png_url,
		img_small_url = img_small_url)