from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.ShopView.as_view(),name='shop'),
    path('shop/dtdd',views.Shopdtdd.as_view(),name='shopdtdd'),
    path('shop/phu-kien',views.Shoppk.as_view(),name='shoppk'),
    path('shop/laptop',views.ShopLap.as_view(),name='shoplap'),
    path('shop/tablet',views.Shoptab.as_view(),name='shoptab'),
    # path('shop/',views.ShopView.as_view(),name='shop'),
]



