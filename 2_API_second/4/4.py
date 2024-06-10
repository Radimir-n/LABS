def find_southernmost_city():
    cities = input("Введите названия городов через запятую: ").split(',')
    min_latitude = 90
    southernmost_city = ""
    for city in cities:
        city_name = city.strip()
        latitude = float(input(f"Введите широту для города {city_name}: "))
        
        if latitude < min_latitude:
            min_latitude = latitude
            southernmost_city = city_name  

    print(f"Самый южный город из введенных: {southernmost_city}")
if __name__ == "__main__":
    find_southernmost_city()
