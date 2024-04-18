import json
import requests
from epicgame_info_wrapper import *
from apikeys import *


def fetch_data():
    try:
        response = requests.get(EPIC_GAMES_KEY)
        if response.status_code == 200:
            print('Api working\n _______________')
            data = json.loads(response.text)
            return data
        else:
            print('API not working\n _______________')
    
    except:
        print("Invalid API")



def fetch_games_embed():
    data = fetch_data()
    elements = data['data']['Catalog']['searchStore']['elements']
    gamelist = []

    for element in elements:
        if element['promotions']['promotionalOffers'] and element['price']['totalPrice']['discountPrice'] == 0:
            gamelist.append(GameInfoWrapper(element).game_info_embed())

    return gamelist



def fetch_free_games():
    data = fetch_data()
    elements = data['data']['Catalog']['searchStore']['elements']
    gamelist = []

    for element in elements:
        if element['promotions']['promotionalOffers'] and element['price']['totalPrice']['discountPrice'] == 0:
            gamelist.append(GameInfoWrapper(element))

    return gamelist
