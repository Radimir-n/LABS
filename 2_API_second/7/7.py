import requests

def find_district(address):
    api_key = '3d8d59aa-3220-4de8-8596-5a1dc8aa9be7'

    try:
        geocode_response = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&format=json&geocode={address}')
        geocode_data = geocode_response.json()

        coordinates = geocode_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        longitude, latitude = map(float, coordinates.split())

        district_response = requests.get(f'https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&format=json&geocode={longitude},{latitude}&kind=district')
        district_data = district_response.json()

        district = district_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']

        return district
    except Exception as e:
        return "Ошибка при определении района:", str(e)

if __name__ == "__main__":
    address = input("Введите адрес: ")
    result = find_district(address)
    print("Район, в котором находится адрес:", result)