from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from filter.cart.forms import CartAddProductForm
from django.template.context_processors import csrf
from django.views.generic import View

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


class tele(View):
    def get(self, request, *args, **kwargs):
        if request.GET.get('name') == "Ф И О":
            a = {"name": None}
            telegram.update(a)
        else:
            a = {"name": request.GET.get('name')}
            telegram.update(a)
        if request.GET.get('mail') == "E-mail":
            a = {"mail": None}
            telegram.update(a)
        else:
            a = {"mail": request.GET.get('mail')}
            telegram.update(a)
        if request.GET.get('phone') == "Мобильный телефон":
            a = {"phone": None}
            telegram.update(a)
        else:
            a = {"phone": request.GET.get('phone')}
            telegram.update(a)
        if request.GET.get('street') == "Адрес доставки":
            a = {"street": None}
            telegram.update(a)
        else:
            a = {"street": request.GET.get('street')}
            telegram.update(a)
        if request.GET.get('comm') == "Комментарий":
            a = {"comm": None}
            telegram.update(a)
        else:
            a = {"comm": request.GET.get('comm')}
            telegram.update(a)



        print(telegram)

        # text = """
        # Имя: %s
        # Телефон: %s
        # Комментарий: %s
        # Количество токенов: %s
        # Email: %s
        # """ % (_name, _phone, _comments, _tokens, _email)
        # print(text)
        # if _name or _phone or _comments:
        #     url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=167315364&text=%s" % (text)
        #     requests.post(url)   
        #     url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=70025022&text=%s" % (text)
        #     requests.post(url)   
        #     url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=65472004&text=%s" % (text)
        #     requests.post(url)   
        #     url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=-303230127&text=%s" % (text)
        #     requests.post(url)   
        #     url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=34436430&text=%s" % (text)
        #     requests.post(url)   
        #     url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=27390261&text=%s" % (text)
        #     requests.post(url) 
        # return render_template('ok.html', users = len(sad()) - 1, koll = sad()[0][1] - 9607)

        return render(request, '/shop/product/list.html')










