import folium
import random
import geopy
from geopy.geocoders import Nominatim

# Ваш API ключ
API_KEY = "3d8d59aa-3220-4de8-8596-5a1dc8aa9be7"

# Список городов
cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Нижний Новгород", "Казань", "Челябинск", "Омск", "Самара", "Ростов-на-Дону"]

def get_random_city():
    return random.choice(cities)

def get_random_map_part(city):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(city)
    zoom = random.randint(12, 15)
    width = random.randint(200, 400)
    height = random.randint(200, 400)
    offset = random.randint(-width // 2, width // 2), random.randint(-height // 2, height // 2)

    map = folium.Map(location=[location.latitude, location.longitude], zoom_start=zoom)

    folium.Rectangle(bounds=[[location.latitude + offset[0], location.longitude + offset[1]],
                            [location.latitude + offset[0] + width, location.longitude + offset[1] + height]], color="red").add_to(map)

    if random.random() < 0.5:
        folium.TileLayer('cartodbpositron').add_to(map)
    else:
        folium.TileLayer('satellite').add_to(map)

    map.save(f"{city}.html")

city = get_random_city()
get_random_map_part(city)