from django.urls import path
from . import views
urlpatterns = [
	path('', views.index),
	path('search', views.process_search),
	path('results', views.display_results),
	path('card/<int:cardid>', views.single_card_view),
	path('login', views.login),
	path('logout',views.logout),
	path('decks', views.load_user_decks_page),
	path('deck/<int:deckid>', views.load_single_deck),
	path('new_deck', views.add_deck)
]