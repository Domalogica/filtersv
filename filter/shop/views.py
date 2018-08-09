from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from filter.cart.forms import CartAddProductForm
from django.template.context_processors import csrf
from django.views.generic import View
import requests

# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })
# Страница товара
# def ProductDetail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     return render_to_response('shop/product/detail.html',
#                              {'product': product,
#                               'cart_product_form': cart_product_form})

def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    context.update(csrf(request))
    return render_to_response('shop/product/detail.html', context)


telegram = {}



def teles(request):
    return render(request, 'main.html')



def tele(request):
    if request.POST:
        if request.POST.get('name') == "Ф И О":
            a = {"name": None}
            telegram.update(a)
        else:
            a = {"name": request.POST.get('name')}
            telegram.update(a)
        if request.POST.get('mail') == "E-mail":
            a = {"mail": None}
            telegram.update(a)
        else:
            a = {"mail": request.POST.get('mail')}
            telegram.update(a)
        if request.POST.get('phone') == "Мобильный телефон":
            a = {"phone": None}
            telegram.update(a)
        else:
            a = {"phone": request.POST.get('phone')}
            telegram.update(a)
        if request.POST.get('street') == "Адрес доставки":
            a = {"street": None}
            telegram.update(a)
        else:
            a = {"street": request.POST.get('street')}
            telegram.update(a)
        if request.POST.get('comm') == "Комментарий":
            a = {"comm": None}
            telegram.update(a)
        else:
            a = {"comm": request.POST.get('comm')}
            telegram.update(a)



        print(telegram)

        text = """
        Имя: %s
    Телефон: %s
    Почта: %s
    Адрес: %s
    Комментарий: %s
        """ % (telegram['name'], telegram['phone'], telegram['mail'], telegram['street'], telegram['comm'])
        print(text)
        if telegram['name']:
            url = "https://api.telegram.org/bot674994528:AAGIH14UqG-11arwRTtFmbPhKS0wID-Xr4E/sendMessage?chat_id=167315364&text=%s" % (text)
            requests.post(url)   
            url = "https://api.telegram.org/bot674994528:AAGIH14UqG-11arwRTtFmbPhKS0wID-Xr4E/sendMessage?chat_id=70025022&text=%s" % (text)
            requests.post(url)   
            url = "https://api.telegram.org/bot674994528:AAGIH14UqG-11arwRTtFmbPhKS0wID-Xr4E/sendMessage?chat_id=65472004&text=%s" % (text)
            requests.post(url)   
            url = "https://api.telegram.org/bot674994528:AAGIH14UqG-11arwRTtFmbPhKS0wID-Xr4E/sendMessage?chat_id=-303230127&text=%s" % (text)
            requests.post(url)   
            url = "https://api.telegram.org/bot674994528:AAGIH14UqG-11arwRTtFmbPhKS0wID-Xr4E/sendMessage?chat_id=34436430&text=%s" % (text)
            requests.post(url)   
            url = "https://api.telegram.org/bot674994528:AAGIH14UqG-11arwRTtFmbPhKS0wID-Xr4E/sendMessage?chat_id=27390261&text=%s" % (text)
            requests.post(url) 

        return render(request, 'main.html', {})
    else:
        return render(request, 'main.html', {})









