Спартак
Динамо
Лужники
Полезным будет использование словаря с координатами
stadiums_location = {"Лужники": "37.554191,55.715551",
                     "Спартак": "37.440262,55.818015",
                     "Динамо": "37.559809,55.791540"
                     }

import folium
# Координаты центра Москвы
moscow_center = (55.755826, 37.6173)

# Координаты стадионов
stadiums_location = {"Лужники": "37.554191,55.715551",
                    "Спартак": "37.440262,55.818015",
                    "Динамо": "37.559809,55.791540"
                    }
# Создаем карту
map = folium.Map(location=moscow_center, zoom_start=11)

# Добавляем метки стадионов на карту
for stadium, location in stadiums_location.items():
    coords = location.split(",")
    folium.Marker(location=[float(coords[1]), 
    float(coords[0])], popup=stadium).add_to(map)
# Сохраняем карту в HTML файл
map.save("moscow_stadiums_map.html")
