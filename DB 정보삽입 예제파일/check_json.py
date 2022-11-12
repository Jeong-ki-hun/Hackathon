import json

with open('static/json/file_name.json') as json_file:
     fd = json.load(json_file)

json_12 = fd['data']
a = []
for i in json_12:
     content = {
                "title":i['식당명'],
                "mapx": str(i['식당위도']),
                "mapy": str(i['식당경도']),
            }
     a.append(content)

print(a)