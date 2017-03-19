from django.shortcuts import render
from .models import Goods
# Create your views here.
def index(request):
    goods = Goods.objects.all()
    context = {'goods':goods}
    return render(request, 'goods/index.html', context)
