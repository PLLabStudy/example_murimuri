from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    a = "안녕하세요 인덱스 페이지입니다!."
    send_varible = {
        'B' : " 안녕하세요 인덱스 풰이쥐입니다!.", 
        'a' : a}
    return render(request, "index.html", send_varible)

    