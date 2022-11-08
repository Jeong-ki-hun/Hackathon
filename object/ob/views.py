from django.shortcuts import render
from django.http import Http404
from .models import Question, ShopList, SeoulTable
import json

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'ob/index.html', context)

def shop_list(request):
    data = ShopList.objects.all()
    return render(request, 'ob/index_3.html', {'data' : data})

def map(request):
    with open('static/json/file_name.json', encoding='utf-8') as json_file:
        js = json.load(json_file)
        js = js['data']
        seoul_t = []
    for i in js:
        content = {
                "title":i['식당명'],
                "mapx": str(i['식당경도']),
                "mapy": str(i['식당위도']),
            }
        seoul_t.append(content)

    seoul = json.dumps(seoul_t, ensure_ascii=False)
    return render(request,'ob/map.html',{'seoul':seoul})
  
