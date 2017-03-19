from django.shortcuts import render
from .models import ShoppingCart
from goods.models import Goods
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    # 获取当前用户的购物车
    cart_now = ShoppingCart.objects.filter(whoscart=request.user)
    # 获取当前购物车的货物
    goods = Goods.objects.filter(shoppingcart=cart_now)
    context = {'goods':goods}
    return render(request, 'shoppingcart/index.html',context)
