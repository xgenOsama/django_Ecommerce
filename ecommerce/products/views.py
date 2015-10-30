from django.shortcuts import render
from django.http import Http404
from marketing.models import MarketingMessage
from .models import Product, ProductImage


# Create your views here.

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query': q, 'products': products}
        template = 'products/results.html'
    else:
        context = {}
        template = 'products/home.html'
    return render(request, template, context)


def home(request):
    try:
        request.session['marketing_message'] = MarketingMessage.objects.get_featured_item().message
    except:
        request.session['marketing_message'] = False
    products = Product.objects.all()
    context = {
        'products': products
    }
    template = 'products/home.html'
    return render(request, template, context)


def all(request):
    request.session['marketing_message'] = False
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        images = product.productimage_set.all()
        context = {'product': product, "images": images}
        template = 'products/single.html'
        return render(request, template, context)
    except:
        raise Http404
