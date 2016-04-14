#coding:utf-8
from django.http import HttpResponse
import datetime as dt

def hello(request):
    return HttpResponse("彩云老婆,我爱你!")

def current_time(request):
    now = dt.datetime.now()
    html = "<html><body>现在时间是%s</body></html>"%now
    return HttpResponse(html)