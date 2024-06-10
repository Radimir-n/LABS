import folium
from geopy.distance import geodesic

# Координаты городов
cities = {
    "Уфа": (54.738227, 55.972065),
    "Санкт-Петербург": (59.934280, 30.335098),
    "Москва": (55.755826, 37.617300),
    "Казань": (55.796127, 49.106405)
}

# Строим путь и вычисляем его длину
route_points = [cities["Уфа"], cities["Санкт-Петербург"], cities["Москва"], cities["Казань"]]
route_length = sum(geodesic(route_points[i], route_points[i + 1]).kilometers for i in range(len(route_points) - 1)

# Находим среднюю точку пути
mean_lat = sum(coord[0] for coord in route_points) / len(route_points)
mean_lon = sum(coord[1] for coord in route_points) / len(route_points)

# Создаем карту
map = folium.Map(location=[mean_lat, mean_lon], zoom_start=6)

# Добавляем метку в среднюю точку пути
folium.Marker(location=[mean_lat, mean_lon], popup="Средняя точка пути").add_to(map)

# Построение пути
folium.PolyLine(route_points, color="blue", weight=2.5, opacity=1).add_to(map)

# Сохраняем карту в HTML файл
map.save("route_map.html")

# Отображаем карту
map
