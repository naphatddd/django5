from django.shortcuts import render, redirect
from .models import tb_news3
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'web/index.html')


def formdata(request):
    return render(request, 'web/formdata.html')


def addnewsdata(request):
    news_title = request.POST['news_title']
    news_detail = request.POST['news_detail']
    news_center = request.POST['news_center']
    news_photo = request.FILES['news_photo']

    content = tb_news3(news_title=news_title, news_detail=news_detail,
                       news_center=news_center, news_photo=news_photo)
    content.save()
    return redirect('/contentnewsdata')


def contentnewsdata(request):
    mynewsdata = tb_news3.objects.all()
    return render(request, 'web/contentnewsdata.html', {'news': mynewsdata})


def contentedit(request):
    id = request.GET['id']
    result = tb_news3.objects.filter(pk=id)
    return render(request, 'web/contentedit.html', {'result': result})


def contentupdate(request):
    id = request.POST['id']
    news_title = request.POST['news_title']
    news_detail = request.POST['news_detail']
    news_center = request.POST['news_center']
    try:
        news_photo = request.FILES['news_photo']
    except KeyError:
        news_photo = None
    content = tb_news3.objects.get(pk=id)
    content.news_title = news_title
    content.news_detail = news_detail
    content.news_center = news_center
    if news_photo is not None:
        content.news_photo = news_photo

    content.save()
    return redirect('/contentnewsdata')

def contentdel(request):
    id = request.POST['id']
    content = tb_news3.objects.get(pk=id)
    content.delete()
    return redirect('/contentnewsdata')
