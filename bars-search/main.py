import requests
import json
import folium
from os import getenv
from pprint import pprint
from geopy import distance
from flask import Flask

NEAREST_BARS_AMOUNT = 5

APIKEY = getenv('APIKEY')

def fetch_coordinates(apikey, place):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    params = {"geocode": place, "apikey": apikey, "format": "json"}
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    places_found = response.json()['response']['GeoObjectCollection']['featureMember']
    most_relevant = places_found[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat
# Спасибо, Олег! Лучше и не назвать
def get_bar_distance(distance):
  return distance['distance']

def bars_search():
  with open('found_bars.html') as file:
    return file.read()

def main():
  with open('bars.json', 'r', encoding='CP1251') as bars_file:
    bars_content = json.loads(bars_file.read())

  place = input('Где вы находитесь? ')
  location = fetch_coordinates(APIKEY, place)[::-1]
  print('Ваши координаты:', location)

  bars = []
  for bar in bars_content:
    bar_info = {}
    latitude = bar['Latitude_WGS84']
    longitude = bar['Longitude_WGS84']
    bar_coord = (latitude, longitude)
    bar_info={
      'title': bar['Name'],
      'latitude': latitude,
      'longitude': longitude,
      'distance': distance.distance(location, bar_coord).km
    }
    bars.append(bar_info)

  nearest_bars = sorted(bars, key=get_bar_distance)[:NEAREST_BARS_AMOUNT]

  bar_map = folium.Map(location=location,
                  zoom_start=10)
  tooltip = 'Нажми меня!'
  for place in nearest_bars:
    coordinates = (place['latitude'], place['longitude'])
    folium.Marker(coordinates, popup=place['title'], tooltip=tooltip).add_to(bar_map)
  bar_map.save('found_bars.html')

  app = Flask(__name__)
  app.add_url_rule('/', 'Where_is_bar?', bars_search)
  app.run('0.0.0.0')

if __name__=='__main__':
  main()