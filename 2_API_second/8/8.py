import math

# Функция для вычисления расстояния между двумя точками на градусной сетке
def calculate_distance(lat1, lon1, lat2, lon2):
    # Преобразование широты и долготы из градусов в радианы
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Приближенная декартова метрика для расчета расстояния
    distance = math.sqrt((111 * (lat2 - lat1))**2 + (111 * math.cos((lat1 + lat2) / 2) * (lon2 - lon1))**2)
    
    return distance

# Ввод координат дома и университета
print("Введите координаты вашего дома:")
home_lat = float(input("Широта дома: "))
home_lon = float(input("Долгота дома: "))

print("Введите координаты университета:")
uni_lat = float(input("Широта университета: "))
uni_lon = float(input("Долгота университета: "))

# Вычисление расстояния и его вывод
distance = calculate_distance(home_lat, home_lon, uni_lat, uni_lon)
print(f"Расстояние от дома до университета приблизительно составляет {int(distance)} метров.")
