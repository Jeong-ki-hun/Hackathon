import json
import urllib.request



URL = 'https://api.odcloud.kr/api/15076742/v1/uddi:e4eae9ea-7beb-429f-a089-99356696d6f7?page=1&perPage=3400&returnType=JSON&serviceKey=qBIWS4oXVGK2hiMzXjXQ%2BRu%2Bpc3WIWnp1IRIprMmP0j8u542GMc2lyqdEeaOS0O3NFD1p6vS8%2BWCEIiXUa1jAw%3D%3D'
json_page = urllib.request.urlopen(URL)
json_data = json_page.read().decode('utf-8')
json_array = json.loads(json_data)

print(json_array)

save_file = open('./file_name.json','w')
json.dump(json_array, save_file,ensure_ascii=False)
save_file.close()

# with open('file_name.json') as json_file:
#     data = json.load(json_file)

# print(data)