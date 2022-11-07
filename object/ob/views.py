from django.shortcuts import render
from django.http import Http404
from .models import Question, ShopList, SeoulTable


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'ob/index.html', context)

def shop_list(request):
    data = ShopList.objects.all()
    return render(request, 'ob/index_3.html', {'data' : data})

def map(request):
    seoul = SeoulTable.objects.all()
    return render(request,'ob/map.html',{'seoul':seoul})
  
