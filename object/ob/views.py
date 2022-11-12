from django.shortcuts import render
from django.http import Http404
from .models import Question, ObResttable, SeoulTable
import json
from django.core.paginator import Paginator

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'ob/index_5.html', context)

def shop_list(request):
    data = ObResttable.objects.all()
    page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(data, '10') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'ob/index_3.html', {'page_obj' : page_obj})

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

def Dashborad(request):
    return render(request,'ob/Dash/index.html')
