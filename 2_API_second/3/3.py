import requests
from PIL import Image

def save_satellite_image(lat, lon):
    api_key = "3d8d59aa-3220-4de8-8596-5a1dc8aa9be7"
    url = f"https://maps.yandex.ru/map-kit/v2/tiles/air/{lat},{lon},15/sat,skl?apikey={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.save("satellite_image.png")
        print("Спутниковый снимок успешно сохранен в файл satellite_image.png")
    else:
        print("Не удалось получить спутниковый снимок")

if __name__ == "__main__":
    latitude = float(input("Введите широту объекта: "))
    longitude = float(input("Введите долготу объекта: "))

    save_satellite_image(latitude, longitude)