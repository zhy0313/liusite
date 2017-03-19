from django.db import models
from shoppingcart.models import ShoppingCart
# Create your models here.
class Goods(models.Model):
    shoppingcart = models.ForeignKey(ShoppingCart)
    goods_info = models.CharField("商品简介信息",max_length=500)
    goods_pic = models.CharField("展示界面的商品图标位置,多个图片位置以;分割", max_length=5000)
    goods_url = models.CharField("商品详情位置", max_length=300)
    
    def __str__(self):
        return "商品信息页面"
