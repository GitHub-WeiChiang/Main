from django.http import HttpResponse

def index(request):
    return HttpResponse("这里是 weichiangblog.com 的投票站点")
