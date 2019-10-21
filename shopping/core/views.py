

# Create your views here.
from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from product.models import Product, Category
class HomeView(View):
    def get(self,request):
        return render(request,'homepage/index.html')


class ShopView(View):
    def get(self,request):
        productList=Product.objects.all()
        print(len(productList))
        listLength=len(productList)
        return render(request,'homepage/shop.html',{"l":listLength,"pl":productList})

class Shopdtdd(View):
    def get(self,request):
        cate=Category.objects.get(title='Điện Thoại')
        pl=cate.product_set.all()
        # productList.category_set.
        print(len(pl))
        listLength=len(pl)
        return render(request,'homepage/shopdtdd.html',{"l":listLength,"pl":pl})

class Shoptab(View):
    def get(self,request):
        cate=Category.objects.get(title='Tablet')
        pl=cate.product_set.all()
        # productList.category_set.
        print(len(pl))
        listLength=len(pl)
        return render(request,'homepage/shoptab.html',{"l":listLength,"pl":pl})

class ShopLap(View):
    def get(self,request):
        cate=Category.objects.get(title='Laptop')
        pl=cate.product_set.all()
        # productList.category_set.
        print(len(pl))
        listLength=len(pl)
        return render(request,'homepage/shoplap.html',{"l":listLength,"pl":pl})


class Shoppk(View):
    def get(self,request):
        cate=Category.objects.get(title='Phụ Kiện')
        pl=cate.product_set.all()
        # productList.category_set.
        print(len(pl))
        listLength=len(pl)
        return render(request,'homepage/shoppk.html',{"l":listLength,"pl":pl})

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'homepage/register.html', {'form': form})
