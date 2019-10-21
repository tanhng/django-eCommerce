"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user import views as user_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('register/',user_view.register,name='register'),
    path('login/',user_view.loginn.as_view(),name='login'),
    path('logout/',user_view.logout_request,name='logout'),
    path('cart/',user_view.cartView.as_view(),name='cartView'),
    path('addtocart/<int:product_id>/',user_view.add_to_cart,name='update_cart'),
    path('clearcart/',user_view.clearCart,name='clear_cart'),
    path('staff/',user_view.testStaff,name='teststaff'),
]
