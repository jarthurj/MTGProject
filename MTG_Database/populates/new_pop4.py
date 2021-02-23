import json
from mtg_app.models import *
with open("./newmtgdatabase.json") as file:
	card_data = json.load(file)

def prepstr(str):# preps the string for being an attribute to the card
	str = str.lower()
	str = str.replace(' ',"_")
	str = str.replace("'","")
	return str
def prepstr2(str):# preps the string for geting the keyword object
	str = str.replace(' ',"_")
	str = str.replace("'","")
	str = str.replace("-","_")
	return str

keyword_dict = {
'Artifact':[],
'Conspiracy':[],
'Creature':[],
'Enchantment':[],
'Instant':[],
'Land':[],
'Phenomenon':[],
'Plane':[],
'Planeswalker':[],
'Scheme':[],
'Sorcery':[],
'Tribal':[],
'Vanguard':[],
'Adamant':[],
'Adapt':[],
'Addendum':[],
'Affinity':[],
'Afflict':[],
'Afterlife':[],
'Aftermath':[],
'Amass':[],
'Amplify':[],
'Annihilator':[],
'Ascend':[],
'Assemble':[],
'Assist':[],
'Augment':[],
'Aura Swap':[],
'Awaken':[],
'Banding':[],
'Basic landcycling':[],
'Battalion':[],
'Battle Cry':[],
'Bestow':[],
'Bloodrush':[],
'Bloodthirst':[],
'Boast':[],
'Bolster':[],
'Bushido':[],
'Buyback':[],
'Cascade':[],
'Champion':[],
'Changeling':[],
'Channel':[],
'Chroma':[],
'Cipher':[],
'Clash':[],
'Cohort':[],
'Commander ninjutsu':[],
'Companion':[],
'Conspire':[],
'Constellation':[],
'Converge':[],
'Convoke':[],
"Council's dilemma":[],
'Crew':[],
'Cumulative upkeep':[],
'Cycling':[],
'Dash':[],
'Deathtouch':[],
'Defender':[],
'Delirium':[],
'Delve':[],
'Desertwalk':[],
'Detain':[],
'Dethrone':[],
'Devoid':[],
'Devour':[],
'Domain':[],
'Double strike':[],
'Dredge':[],
'Echo':[],
'Embalm':[],
'Emerge':[],
'Eminence':[],
'Enchant':[],
'Enrage':[],
'Entwine':[],
'Epic':[],
'Equip':[],
'Escalate':[],
'Escape':[],
'Eternalize':[],
'Evoke':[],
'Evolve':[],
'Exalted':[],
'Exert':[],
'Exploit':[],
'Explore':[],
'Extort':[],
'Fabricate':[],
'Fading':[],
'Fateful hour':[],
'Fateseal':[],
'Fear':[],
'Ferocious':[],
'Fight':[],
'First strike':[],
'Flanking':[],
'Flash':[],
'Flashback':[],
'Flying':[],
'Forecast':[],
'Forestcycling':[],
'Forestwalk':[],
'Foretell':[],
'Formidable':[],
'Fortify':[],
'Fuse':[],
'Goad':[],
'Graft':[],
'Grandeur':[],
'Gravestorm':[],
'Haste':[],
'Haunt':[],
'Hellbent':[],
"Hero's Reward":[],
'Heroic':[],
'Hexproof':[],
'Hexproof from':[],
'Hidden agenda':[],
'Hideaway':[],
'Horsemanship':[],
'Imprint':[],
'Improvise':[],
'Indestructible':[],
'Infect':[],
'Ingest':[],
'Inspired':[],
'Intimidate':[],
'Investigate':[],
'Islandcycling':[],
'Islandwalk':[],
'Join forces':[],
'Jump-start':[],
'Kicker':[],
'Kinfall':[],
'Kinship':[],
'Landcycling':[],
'Landfall':[],
'Landship':[],
'Landwalk':[],
'Legacy':[],
'Legendary landwalk':[],
'Level Up':[],
'Lieutenant':[],
'Lifelink':[],
'Living weapon':[],
'Madness':[],
'Manifest':[],
'Megamorph':[],
'Meld':[],
'Melee':[],
'Menace':[],
'Mentor':[],
'Metalcraft':[],
'Mill':[],
'Miracle':[],
'Modular':[],
'Monstrosity':[],
'Morbid':[],
'Morph':[],
'Mountaincycling':[],
'Mountainwalk':[],
'Multikicker':[],
'Mutate':[],
'Myriad':[],
'Ninjutsu':[],
'Nonbasic landwalk':[],
'Outlast':[],
'Overload':[],
'Parley':[],
'Partner':[],
'Partner with':[],
'Persist':[],
'Phasing':[],
'Plainscycling':[],
'Plainswalk':[],
'Populate':[],
'Proliferate':[],
'Protection':[],
'Provoke':[],
'Prowess':[],
'Prowl':[],
'Radiance':[],
'Raid':[],
'Rally':[],
'Rampage':[],
'Reach':[],
'Rebound':[],
'Recover':[],
'Reinforce':[],
'Renown':[],
'Replicate':[],
'Retrace':[],
'Revolt':[],
'Riot':[],
'Ripple':[],
'Scavenge':[],
'Scry':[],
'Shadow':[],
'Shroud':[],
'Skulk':[],
'Slivercycling':[],
'Soulbond':[],
'Soulshift':[],
'Spectacle':[],
'Spell mastery':[],
'Splice':[],
'Split second':[],
'Storm':[],
'Strive':[],
'Sunburst':[],
'Support':[],
'Surge':[],
'Surveil':[],
'Suspend':[],
'Swampcycling':[],
'Swampwalk':[],
'Sweep':[],
'Tempting offer':[],
'Threshold':[],
'Totem armor':[],
'Trample':[],
'Transfigure':[],
'Transform':[],
'Transmute':[],
'Tribute':[],
'Typecycling':[],
'Undaunted':[],
'Underdog':[],
'Undergrowth':[],
'Undying':[],
'Unearth':[],
'Unleash':[],
'Vanishing':[],
'Vigilance':[],
'Will of the council':[],
'Wither':[],
'Wizardcycling':[],
}

for card in card_data:
	try:
		card_keywords = ','.join(card['keywords'])
	except:
		pass
	try:
		card_type = card['type_line']
	except:
		pass
	try:
		name = card['name']
	except:
		pass
	try:
		card_id = card['id']
	except:
		pass
	try:
		flavor_text = card['flavor_text']
	except:
		pass
	try:
		oracle_text =card['oracle_text']
	except:
		pass
	try:
		img_art_crop_url = card['image_uris']['art_crop']
	except:
		pass
	try:
		img_border_crop_url = card['image_uris']['border_crop']
	except:
		pass
	try:
		img_large_url = card['image_uris']['large']
	except:
		pass
	try:
		img_png_url = card['image_uris']['png']
	except:
		pass
	try:
		img_small_url = card['image_uris']['small']
	except:
		pass
	card_type = card_type.lower()
	new_card = Card.objects.create(
		name = name,
		card_id = card_id,
		flavor_text = flavor_text,
		oracle_text = oracle_text,
		img_art_crop_url = img_art_crop_url,
		img_border_crop_url = img_border_crop_url,
		img_large_url = img_large_url,
		img_png_url = img_png_url,
		img_small_url = img_small_url,
		card_keywords = card_keywords,
		card_type = card_type
	)
	for key in card['keywords']:
		keyword_dict[key].append(new_card)

	if "artifact" in card_type:
		keyword_dict["Artifact"].append(new_card)
	if "conspiracy" in card_type:
		keyword_dict["Conspiracy"].append(new_card)
	if "creature" in card_type:
		keyword_dict["Creature"].append(new_card)
	if "enchantment" in card_type:
		keyword_dict["Enchantment"].append(new_card)
	if "instant" in card_type:
		keyword_dict["Instant"].append(new_card)
	if "land" in card_type:
		keyword_dict["Land"].append(new_card)
	if "phenomenon" in card_type:
		keyword_dict["Phenomenon"].append(new_card)
	if "plane" in card_type:
		keyword_dict["Plane"].append(new_card)
	if "planeswalker" in card_type:
		keyword_dict["Planeswalker"].append(new_card)
	if "scheme" in card_type:
		keyword_dict["Scheme"].append(new_card)
	if "sorcery" in card_type:
		keyword_dict["Sorcery"].append(new_card)
	if "tribal" in card_type:
		keyword_dict["Tribal"].append(new_card)
	if "vanguard" in card_type:
		keyword_dict["Vanguard"].append(new_card)


# for thing in keyword_dict:
	
# 	if thing != "Jump-start":
# 		print(thing,prepstr(thing),prepstr2(thing))
# 		prepped_att= eval(prepstr(thing))
# 		prepped_att_cap = eval(prepstr2(thing))
# 		print(prepped_att, prepped_att_cap)
# 		for card in keyword_dict[thing]:
# 			# attribute = eval(prepped_att)
# 			key_object = prepped_att_cap.objects.first()
# 			card.prepped_att = key_object
# 			card.save()
for card in keyword_dict['Artifact']:
	card.artifact = Artifact.objects.first()
	card.save()
for card in keyword_dict['Conspiracy']:	
	card.conspiracy = Conspiracy.objects.first()
	card.save()
for card in keyword_dict['Creature']:	
	card.creature = Creature.objects.first()
	card.save()
for card in keyword_dict['Enchantment']:	
	card.enchantment = Enchantment.objects.first()
	card.save()
for card in keyword_dict['Instant']:	
	card.instant = Instant.objects.first()
	card.save()
for card in keyword_dict['Land']:	
	card.land = Land.objects.first()
	card.save()
for card in keyword_dict['Phenomenon']:	
	card.phenomenon = Phenomenon.objects.first()
	card.save()
for card in keyword_dict['Plane']:	
	card.plane = Plane.objects.first()
	card.save()
for card in keyword_dict['Planeswalker']:	
	card.planeswalker = Planeswalker.objects.first()
	card.save()
for card in keyword_dict['Scheme']:	
	card.scheme = Scheme.objects.first()
	card.save()
for card in keyword_dict['Sorcery']:	
	card.sorcery = Sorcery.objects.first()
	card.save()
for card in keyword_dict['Tribal']:	
	card.tribal = Tribal.objects.first()
	card.save()
for card in keyword_dict['Vanguard']:	
	card.vanguard = Vanguard.objects.first()
	card.save()
for card in keyword_dict['Adamant']:	
	card.adamant = Adamant.objects.first()
	card.save()
for card in keyword_dict['Adapt']:	
	card.adapt = Adapt.objects.first()
	card.save()
for card in keyword_dict['Addendum']:	
	card.addendum = Addendum.objects.first()
	card.save()
for card in keyword_dict['Affinity']:	
	card.affinity = Affinity.objects.first()
	card.save()
for card in keyword_dict['Afflict']:	
	card.afflict = Afflict.objects.first()
	card.save()
for card in keyword_dict['Afterlife']:	
	card.afterlife = Afterlife.objects.first()
	card.save()
for card in keyword_dict['Aftermath']:	
	card.aftermath = Aftermath.objects.first()
	card.save()
for card in keyword_dict['Amass']:	
	card.amass = Amass.objects.first()
	card.save()
for card in keyword_dict['Amplify']:	
	card.amplify = Amplify.objects.first()
	card.save()
for card in keyword_dict['Annihilator']:	
	card.annihilator = Annihilator.objects.first()
	card.save()
for card in keyword_dict['Ascend']:	
	card.ascend = Ascend.objects.first()
	card.save()
for card in keyword_dict['Assemble']:	
	card.assemble = Assemble.objects.first()
	card.save()
for card in keyword_dict['Assist']:	
	card.assist = Assist.objects.first()
	card.save()
for card in keyword_dict['Augment']:	
	card.augment = Augment.objects.first()
	card.save()
for card in keyword_dict['Aura Swap']:	
	card.aura_swap = Aura_Swap.objects.first()
	card.save()
for card in keyword_dict['Awaken']:	
	card.awaken = Awaken.objects.first()
	card.save()
for card in keyword_dict['Banding']:	
	card.banding = Banding.objects.first()
	card.save()
for card in keyword_dict['Basic landcycling']:	
	card.basic_landcycling = Basic_landcycling.objects.first()
	card.save()
for card in keyword_dict['Battalion']:	
	card.battalion = Battalion.objects.first()
	card.save()
for card in keyword_dict['Battle Cry']:	
	card.battle_cry = Battle_Cry.objects.first()
	card.save()
for card in keyword_dict['Bestow']:	
	card.bestow = Bestow.objects.first()
	card.save()
for card in keyword_dict['Bloodrush']:	
	card.bloodrush = Bloodrush.objects.first()
	card.save()
for card in keyword_dict['Bloodthirst']:	
	card.bloodthirst = Bloodthirst.objects.first()
	card.save()
for card in keyword_dict['Boast']:	
	card.boast = Boast.objects.first()
	card.save()
for card in keyword_dict['Bolster']:	
	card.bolster = Bolster.objects.first()
	card.save()
for card in keyword_dict['Bushido']:	
	card.bushido = Bushido.objects.first()
	card.save()
for card in keyword_dict['Buyback']:	
	card.buyback = Buyback.objects.first()
	card.save()
for card in keyword_dict['Cascade']:	
	card.cascade = Cascade.objects.first()
	card.save()
for card in keyword_dict['Champion']:	
	card.champion = Champion.objects.first()
	card.save()
for card in keyword_dict['Changeling']:	
	card.changeling = Changeling.objects.first()
	card.save()
for card in keyword_dict['Channel']:	
	card.channel = Channel.objects.first()
	card.save()
for card in keyword_dict['Chroma']:	
	card.chroma = Chroma.objects.first()
	card.save()
for card in keyword_dict['Cipher']:	
	card.cipher = Cipher.objects.first()
	card.save()
for card in keyword_dict['Clash']:	
	card.clash = Clash.objects.first()
	card.save()
for card in keyword_dict['Cohort']:	
	card.cohort = Cohort.objects.first()
	card.save()
for card in keyword_dict['Commander ninjutsu']:	
	card.commander_ninjutsu = Commander_ninjutsu.objects.first()
	card.save()
for card in keyword_dict['Companion']:	
	card.companion = Companion.objects.first()
	card.save()
for card in keyword_dict['Conspire']:	
	card.conspire = Conspire.objects.first()
	card.save()
for card in keyword_dict['Constellation']:	
	card.constellation = Constellation.objects.first()
	card.save()
for card in keyword_dict['Converge']:	
	card.converge = Converge.objects.first()
	card.save()
for card in keyword_dict['Convoke']:	
	card.convoke = Convoke.objects.first()
	card.save()
for card in keyword_dict["Council's dilemma"]:	
	card.councils_dilemma = Councils_dilemma.objects.first()
	card.save()
for card in keyword_dict['Crew']:	
	card.crew = Crew.objects.first()
	card.save()
for card in keyword_dict['Cumulative upkeep']:	
	card.cumulative_upkeep = Cumulative_upkeep.objects.first()
	card.save()
for card in keyword_dict['Cycling']:	
	card.cycling = Cycling.objects.first()
	card.save()
for card in keyword_dict['Dash']:	
	card.dash = Dash.objects.first()
	card.save()
for card in keyword_dict['Deathtouch']:	
	card.deathtouch = Deathtouch.objects.first()
	card.save()
for card in keyword_dict['Defender']:	
	card.defender = Defender.objects.first()
	card.save()
for card in keyword_dict['Delirium']:	
	card.delirium = Delirium.objects.first()
	card.save()
for card in keyword_dict['Delve']:	
	card.delve = Delve.objects.first()
	card.save()
for card in keyword_dict['Desertwalk']:	
	card.desertwalk = Desertwalk.objects.first()
	card.save()
for card in keyword_dict['Detain']:	
	card.detain = Detain.objects.first()
	card.save()
for card in keyword_dict['Dethrone']:	
	card.dethrone = Dethrone.objects.first()
	card.save()
for card in keyword_dict['Devoid']:	
	card.devoid = Devoid.objects.first()
	card.save()
for card in keyword_dict['Devour']:	
	card.devour = Devour.objects.first()
	card.save()
for card in keyword_dict['Domain']:	
	card.domain = Domain.objects.first()
	card.save()
for card in keyword_dict['Double strike']:	
	card.double_strike = Double_strike.objects.first()
	card.save()
for card in keyword_dict['Dredge']:	
	card.dredge = Dredge.objects.first()
	card.save()
for card in keyword_dict['Echo']:	
	card.echo = Echo.objects.first()
	card.save()
for card in keyword_dict['Embalm']:	
	card.embalm = Embalm.objects.first()
	card.save()
for card in keyword_dict['Emerge']:	
	card.emerge = Emerge.objects.first()
	card.save()
for card in keyword_dict['Eminence']:	
	card.eminence = Eminence.objects.first()
	card.save()
for card in keyword_dict['Enchant']:	
	card.enchant = Enchant.objects.first()
	card.save()
for card in keyword_dict['Enrage']:	
	card.enrage = Enrage.objects.first()
	card.save()
for card in keyword_dict['Entwine']:	
	card.entwine = Entwine.objects.first()
	card.save()
for card in keyword_dict['Epic']:	
	card.epic = Epic.objects.first()
	card.save()
for card in keyword_dict['Equip']:	
	card.equip = Equip.objects.first()
	card.save()
for card in keyword_dict['Escalate']:	
	card.escalate = Escalate.objects.first()
	card.save()
for card in keyword_dict['Escape']:	
	card.escape = Escape.objects.first()
	card.save()
for card in keyword_dict['Eternalize']:	
	card.eternalize = Eternalize.objects.first()
	card.save()
for card in keyword_dict['Evoke']:	
	card.evoke = Evoke.objects.first()
	card.save()
for card in keyword_dict['Evolve']:	
	card.evolve = Evolve.objects.first()
	card.save()
for card in keyword_dict['Exalted']:	
	card.exalted = Exalted.objects.first()
	card.save()
for card in keyword_dict['Exert']:	
	card.exert = Exert.objects.first()
	card.save()
for card in keyword_dict['Exploit']:	
	card.exploit = Exploit.objects.first()
	card.save()
for card in keyword_dict['Explore']:	
	card.explore = Explore.objects.first()
	card.save()
for card in keyword_dict['Extort']:	
	card.extort = Extort.objects.first()
	card.save()
for card in keyword_dict['Fabricate']:	
	card.fabricate = Fabricate.objects.first()
	card.save()
for card in keyword_dict['Fading']:	
	card.fading = Fading.objects.first()
	card.save()
for card in keyword_dict['Fateful hour']:	
	card.fateful_hour = Fateful_hour.objects.first()
	card.save()
for card in keyword_dict['Fateseal']:	
	card.fateseal = Fateseal.objects.first()
	card.save()
for card in keyword_dict['Fear']:	
	card.fear = Fear.objects.first()
	card.save()
for card in keyword_dict['Ferocious']:	
	card.ferocious = Ferocious.objects.first()
	card.save()
for card in keyword_dict['Fight']:	
	card.fight = Fight.objects.first()
	card.save()
for card in keyword_dict['First strike']:	
	card.first_strike = First_strike.objects.first()
	card.save()
for card in keyword_dict['Flanking']:	
	card.flanking = Flanking.objects.first()
	card.save()
for card in keyword_dict['Flash']:	
	card.flash = Flash.objects.first()
	card.save()
for card in keyword_dict['Flashback']:	
	card.flashback = Flashback.objects.first()
	card.save()
for card in keyword_dict['Flying']:	
	card.flying = Flying.objects.first()
	card.save()
for card in keyword_dict['Forecast']:	
	card.forecast = Forecast.objects.first()
	card.save()
for card in keyword_dict['Forestcycling']:	
	card.forestcycling = Forestcycling.objects.first()
	card.save()
for card in keyword_dict['Forestwalk']:	
	card.forestwalk = Forestwalk.objects.first()
	card.save()
for card in keyword_dict['Foretell']:	
	card.foretell = Foretell.objects.first()
	card.save()
for card in keyword_dict['Formidable']:	
	card.formidable = Formidable.objects.first()
	card.save()
for card in keyword_dict['Fortify']:	
	card.fortify = Fortify.objects.first()
	card.save()
for card in keyword_dict['Fuse']:	
	card.fuse = Fuse.objects.first()
	card.save()
for card in keyword_dict['Goad']:	
	card.goad = Goad.objects.first()
	card.save()
for card in keyword_dict['Graft']:	
	card.graft = Graft.objects.first()
	card.save()
for card in keyword_dict['Grandeur']:	
	card.grandeur = Grandeur.objects.first()
	card.save()
for card in keyword_dict['Gravestorm']:	
	card.gravestorm = Gravestorm.objects.first()
	card.save()
for card in keyword_dict['Haste']:	
	card.haste = Haste.objects.first()
	card.save()
for card in keyword_dict['Haunt']:	
	card.haunt = Haunt.objects.first()
	card.save()
for card in keyword_dict['Hellbent']:	
	card.hellbent = Hellbent.objects.first()
	card.save()
for card in keyword_dict["Hero's Reward"]:	
	card.heros_Reward = Heros_Reward.objects.first()
	card.save()
for card in keyword_dict['Heroic']:	
	card.heroic = Heroic.objects.first()
	card.save()
for card in keyword_dict['Hexproof']:	
	card.hexproof = Hexproof.objects.first()
	card.save()
for card in keyword_dict['Hexproof from']:	
	card.hexproof_from = Hexproof_from.objects.first()
	card.save()
for card in keyword_dict['Hidden agenda']:	
	card.hidden_agenda = Hidden_agenda.objects.first()
	card.save()
for card in keyword_dict['Hideaway']:	
	card.hideaway = Hideaway.objects.first()
	card.save()
for card in keyword_dict['Horsemanship']:	
	card.horsemanship = Horsemanship.objects.first()
	card.save()
for card in keyword_dict['Imprint']:	
	card.imprint = Imprint.objects.first()
	card.save()
for card in keyword_dict['Improvise']:	
	card.improvise = Improvise.objects.first()
	card.save()
for card in keyword_dict['Indestructible']:	
	card.indestructible = Indestructible.objects.first()
	card.save()
for card in keyword_dict['Infect']:	
	card.infect = Infect.objects.first()
	card.save()
for card in keyword_dict['Ingest']:	
	card.ingest = Ingest.objects.first()
	card.save()
for card in keyword_dict['Inspired']:	
	card.inspired = Inspired.objects.first()
	card.save()
for card in keyword_dict['Intimidate']:	
	card.intimidate = Intimidate.objects.first()
	card.save()
for card in keyword_dict['Investigate']:	
	card.investigate = Investigate.objects.first()
	card.save()
for card in keyword_dict['Islandcycling']:	
	card.islandcycling = Islandcycling.objects.first()
	card.save()
for card in keyword_dict['Islandwalk']:	
	card.islandwalk = Islandwalk.objects.first()
	card.save()
for card in keyword_dict['Join forces']:	
	card.join_forces = Join_forces.objects.first()
	card.save()
for card in keyword_dict['Jump-start']:	
	card.jump_start = Jump_start.objects.first()
	card.save()
for card in keyword_dict['Kicker']:	
	card.kicker = Kicker.objects.first()
	card.save()
for card in keyword_dict['Kinfall']:	
	card.kinfall = Kinfall.objects.first()
	card.save()
for card in keyword_dict['Kinship']:	
	card.kinship = Kinship.objects.first()
	card.save()
for card in keyword_dict['Landcycling']:	
	card.landcycling = Landcycling.objects.first()
	card.save()
for card in keyword_dict['Landfall']:	
	card.landfall = Landfall.objects.first()
	card.save()
for card in keyword_dict['Landship']:	
	card.landship = Landship.objects.first()
	card.save()
for card in keyword_dict['Landwalk']:	
	card.landwalk = Landwalk.objects.first()
	card.save()
for card in keyword_dict['Legacy']:	
	card.legacy = Legacy.objects.first()
	card.save()
for card in keyword_dict['Legendary landwalk']:	
	card.legendary_landwalk = Legendary_landwalk.objects.first()
	card.save()
for card in keyword_dict['Level Up']:	
	card.level_up = Level_Up.objects.first()
	card.save()
for card in keyword_dict['Lieutenant']:	
	card.lieutenant = Lieutenant.objects.first()
	card.save()
for card in keyword_dict['Lifelink']:	
	card.lifelink = Lifelink.objects.first()
	card.save()
for card in keyword_dict['Living weapon']:	
	card.living_weapon = Living_weapon.objects.first()
	card.save()
for card in keyword_dict['Madness']:	
	card.madness = Madness.objects.first()
	card.save()
for card in keyword_dict['Manifest']:	
	card.manifest = Manifest.objects.first()
	card.save()
for card in keyword_dict['Megamorph']:	
	card.megamorph = Megamorph.objects.first()
	card.save()
for card in keyword_dict['Meld']:	
	card.meld = Meld.objects.first()
	card.save()
for card in keyword_dict['Melee']:	
	card.melee = Melee.objects.first()
	card.save()
for card in keyword_dict['Menace']:	
	card.menace = Menace.objects.first()
	card.save()
for card in keyword_dict['Mentor']:	
	card.mentor = Mentor.objects.first()
	card.save()
for card in keyword_dict['Metalcraft']:	
	card.metalcraft = Metalcraft.objects.first()
	card.save()
for card in keyword_dict['Mill']:	
	card.mill = Mill.objects.first()
	card.save()
for card in keyword_dict['Miracle']:	
	card.miracle = Miracle.objects.first()
	card.save()
for card in keyword_dict['Modular']:	
	card.modular = Modular.objects.first()
	card.save()
for card in keyword_dict['Monstrosity']:	
	card.monstrosity = Monstrosity.objects.first()
	card.save()
for card in keyword_dict['Morbid']:	
	card.morbid = Morbid.objects.first()
	card.save()
for card in keyword_dict['Morph']:	
	card.morph = Morph.objects.first()
	card.save()
for card in keyword_dict['Mountaincycling']:	
	card.mountaincycling = Mountaincycling.objects.first()
	card.save()
for card in keyword_dict['Mountainwalk']:	
	card.mountainwalk = Mountainwalk.objects.first()
	card.save()
for card in keyword_dict['Multikicker']:	
	card.multikicker = Multikicker.objects.first()
	card.save()
for card in keyword_dict['Mutate']:	
	card.mutate = Mutate.objects.first()
	card.save()
for card in keyword_dict['Myriad']:	
	card.myriad = Myriad.objects.first()
	card.save()
for card in keyword_dict['Ninjutsu']:	
	card.ninjutsu = Ninjutsu.objects.first()
	card.save()
for card in keyword_dict['Nonbasic landwalk']:	
	card.nonbasic_landwalk = Nonbasic_landwalk.objects.first()
	card.save()
for card in keyword_dict['Outlast']:	
	card.outlast = Outlast.objects.first()
	card.save()
for card in keyword_dict['Overload']:	
	card.overload = Overload.objects.first()
	card.save()
for card in keyword_dict['Parley']:	
	card.parley = Parley.objects.first()
	card.save()
for card in keyword_dict['Partner']:	
	card.partner = Partner.objects.first()
	card.save()
for card in keyword_dict['Partner with']:	
	card.partner_with = Partner_with.objects.first()
	card.save()
for card in keyword_dict['Persist']:	
	card.persist = Persist.objects.first()
	card.save()
for card in keyword_dict['Phasing']:	
	card.phasing = Phasing.objects.first()
	card.save()
for card in keyword_dict['Plainscycling']:	
	card.plainscycling = Plainscycling.objects.first()
	card.save()
for card in keyword_dict['Plainswalk']:	
	card.plainswalk = Plainswalk.objects.first()
	card.save()
for card in keyword_dict['Populate']:	
	card.populate = Populate.objects.first()
	card.save()
for card in keyword_dict['Proliferate']:	
	card.proliferate = Proliferate.objects.first()
	card.save()
for card in keyword_dict['Protection']:	
	card.protection = Protection.objects.first()
	card.save()
for card in keyword_dict['Provoke']:	
	card.provoke = Provoke.objects.first()
	card.save()
for card in keyword_dict['Prowess']:	
	card.prowess = Prowess.objects.first()
	card.save()
for card in keyword_dict['Prowl']:	
	card.prowl = Prowl.objects.first()
	card.save()
for card in keyword_dict['Radiance']:	
	card.radiance = Radiance.objects.first()
	card.save()
for card in keyword_dict['Raid']:	
	card.raid = Raid.objects.first()
	card.save()
for card in keyword_dict['Rally']:	
	card.rally = Rally.objects.first()
	card.save()
for card in keyword_dict['Rampage']:	
	card.rampage = Rampage.objects.first()
	card.save()
for card in keyword_dict['Reach']:	
	card.reach = Reach.objects.first()
	card.save()
for card in keyword_dict['Rebound']:	
	card.rebound = Rebound.objects.first()
	card.save()
for card in keyword_dict['Recover']:	
	card.recover = Recover.objects.first()
	card.save()
for card in keyword_dict['Reinforce']:	
	card.reinforce = Reinforce.objects.first()
	card.save()
for card in keyword_dict['Renown']:	
	card.renown = Renown.objects.first()
	card.save()
for card in keyword_dict['Replicate']:	
	card.replicate = Replicate.objects.first()
	card.save()
for card in keyword_dict['Retrace']:	
	card.retrace = Retrace.objects.first()
	card.save()
for card in keyword_dict['Revolt']:	
	card.revolt = Revolt.objects.first()
	card.save()
for card in keyword_dict['Riot']:	
	card.riot = Riot.objects.first()
	card.save()
for card in keyword_dict['Ripple']:	
	card.ripple = Ripple.objects.first()
	card.save()
for card in keyword_dict['Scavenge']:	
	card.scavenge = Scavenge.objects.first()
	card.save()
for card in keyword_dict['Scry']:	
	card.scry = Scry.objects.first()
	card.save()
for card in keyword_dict['Shadow']:	
	card.shadow = Shadow.objects.first()
	card.save()
for card in keyword_dict['Shroud']:	
	card.shroud = Shroud.objects.first()
	card.save()
for card in keyword_dict['Skulk']:	
	card.skulk = Skulk.objects.first()
	card.save()
for card in keyword_dict['Slivercycling']:	
	card.slivercycling = Slivercycling.objects.first()
	card.save()
for card in keyword_dict['Soulbond']:	
	card.soulbond = Soulbond.objects.first()
	card.save()
for card in keyword_dict['Soulshift']:	
	card.soulshift = Soulshift.objects.first()
	card.save()
for card in keyword_dict['Spectacle']:	
	card.spectacle = Spectacle.objects.first()
	card.save()
for card in keyword_dict['Spell mastery']:	
	card.spell_mastery = Spell_mastery.objects.first()
	card.save()
for card in keyword_dict['Splice']:	
	card.splice = Splice.objects.first()
	card.save()
for card in keyword_dict['Split second']:	
	card.split_second = Split_second.objects.first()
	card.save()
for card in keyword_dict['Storm']:	
	card.storm = Storm.objects.first()
	card.save()
for card in keyword_dict['Strive']:	
	card.strive = Strive.objects.first()
	card.save()
for card in keyword_dict['Sunburst']:	
	card.sunburst = Sunburst.objects.first()
	card.save()
for card in keyword_dict['Support']:	
	card.support = Support.objects.first()
	card.save()
for card in keyword_dict['Surge']:	
	card.surge = Surge.objects.first()
	card.save()
for card in keyword_dict['Surveil']:	
	card.surveil = Surveil.objects.first()
	card.save()
for card in keyword_dict['Suspend']:	
	card.suspend = Suspend.objects.first()
	card.save()
for card in keyword_dict['Swampcycling']:	
	card.swampcycling = Swampcycling.objects.first()
	card.save()
for card in keyword_dict['Swampwalk']:	
	card.swampwalk = Swampwalk.objects.first()
	card.save()
for card in keyword_dict['Sweep']:	
	card.sweep = Sweep.objects.first()
	card.save()
for card in keyword_dict['Tempting offer']:	
	card.tempting_offer = Tempting_offer.objects.first()
	card.save()
for card in keyword_dict['Threshold']:	
	card.threshold = Threshold.objects.first()
	card.save()
for card in keyword_dict['Totem armor']:	
	card.totem_armor = Totem_armor.objects.first()
	card.save()
for card in keyword_dict['Trample']:	
	card.trample = Trample.objects.first()
	card.save()
for card in keyword_dict['Transfigure']:	
	card.transfigure = Transfigure.objects.first()
	card.save()
for card in keyword_dict['Transform']:	
	card.transform = Transform.objects.first()
	card.save()
for card in keyword_dict['Transmute']:	
	card.transmute = Transmute.objects.first()
	card.save()
for card in keyword_dict['Tribute']:	
	card.tribute = Tribute.objects.first()
	card.save()
for card in keyword_dict['Typecycling']:	
	card.typecycling = Typecycling.objects.first()
	card.save()
for card in keyword_dict['Undaunted']:	
	card.undaunted = Undaunted.objects.first()
	card.save()
for card in keyword_dict['Underdog']:	
	card.underdog = Underdog.objects.first()
	card.save()
for card in keyword_dict['Undergrowth']:	
	card.undergrowth = Undergrowth.objects.first()
	card.save()
for card in keyword_dict['Undying']:	
	card.undying = Undying.objects.first()
	card.save()
for card in keyword_dict['Unearth']:	
	card.unearth = Unearth.objects.first()
	card.save()
for card in keyword_dict['Unleash']:	
	card.unleash = Unleash.objects.first()
	card.save()
for card in keyword_dict['Vanishing']:	
	card.vanishing = Vanishing.objects.first()
	card.save()
for card in keyword_dict['Vigilance']:	
	card.vigilance = Vigilance.objects.first()
	card.save()
for card in keyword_dict['Will of the council']:	
	card.will_of_the_council = Will_of_the_council.objects.first() 
	card.save()
for card in keyword_dict['Wither']:	
	card.wither = Wither.objects.first()
	card.save()
for card in keyword_dict['Wizardcycling']:	
	card.wizardcycling = Wizardcycling.objects.first()
	card.save()
