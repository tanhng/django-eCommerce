from django.shortcuts import render,redirect,HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.views import  View
from cart.models import Cart,CartItem
from product.models import Product
from user.models import CustomerUser
def register(request):
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('/')
    else:
        form=SignUpForm()
    return render(request,'homepage/register.html',{'form':form})

class cartView(View):
    def get(self,request):
        print(request.user.id)
        if(len(Cart.objects.filter(user=request.user))==0):
            newCart=Cart(user=request.user)
            newCart.save()
        cart=Cart.objects.get(user=request.user)
        pd=CartItem.objects.filter(cart=cart)
        tong=0
        for x in pd:
            print(x.item.price)
            tong=tong+x.item.price
        return render(request,'homepage/cart.html',{'pd':pd,'tong':tong})
    def post(self,request):
        pass

def clearCart(request):
    cart=Cart.objects.get(user=request.user)
    CartItem.objects.filter(cart=cart).delete()
    return redirect('/cart')


def add_to_cart(request,product_id):
    if(len(Cart.objects.filter(user=request.user))==0):
        newCart=Cart(user=request.user)
        newCart.save()
    print(Cart.objects.filter(user=request.user))
    cart=Cart.objects.get(user=request.user)
    print('cart',cart)
    pd=Product.objects.get(id=product_id)
    print('pd',pd)
    newItem=CartItem.objects.create(item=pd,cart=cart)
    newItem.save()
    return redirect('/')
    
def testStaff(request):
    if not request.user.is_staff:
        return HttpResponse('ban khong phai nhan vien hoac admin nen ban khong co quyen xem trang nay')
    else:
        return HttpResponse('ban la nhan vien hoac admin va ban co quyen xem trang nay')

class loginn(View):
    def get(self,request):
        return render(request,'homepage/login.html')
    def post(self,request):
        name=request.POST.get('userName')
        matkhau=request.POST.get('password')
        userName=authenticate(username=name,password=matkhau)
        print(userName)
        if userName is None:
            return HttpResponse('not exist')
        login(request,userName)
        return redirect("/")

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

            