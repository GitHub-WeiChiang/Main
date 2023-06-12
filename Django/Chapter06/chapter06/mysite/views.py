from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request, tvno=0):
    tv_list = [
        {'name': '中天新聞', 'tvcode': 'oIgbl7t0S_w'},
        {'name': '民視新聞', 'tvcode': 'ylYJSBUgaMA'},
        {'name': '公共電視', 'tvcode': '4Uc00FPs27M'}
    ]

    now = datetime.now()
    tv = tv_list[tvno]

    return render(request, 'index.html', locals())
