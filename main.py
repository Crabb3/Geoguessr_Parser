from geopy.geocoders import Nominatim
import csv

# 定義User-Agent
user_agent = "my_app/1 (https://mywebsite.com; contact@mywebsite.com)"

# 初始化Nominatim Geocoder
geolocator = Nominatim(user_agent=user_agent)

# 查詢地點
with open('output2.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    with open('search_result.csv', 'r', encoding='utf-8') as file:
        line = file.readlines()
        for el in line:
            name = el.split(',')[3]
            try:
                location = geolocator.geocode(name)
                if location:
                    print(f"add {name} success")
                    writer.writerow([location.latitude, location.longitude])
                else:
                    print(f"can not find {name}")
            except:
                continue