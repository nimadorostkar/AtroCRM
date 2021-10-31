from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.contrib.auth.models import User
from .models import Product
from itertools import chain
from django.contrib.auth import get_user_model
from django.db import transaction
from django.urls import reverse
from django.db.models import Q
import datetime







#------------------------------------------------------------------------------
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))






#------------------------------------------------------------------------------
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))





#------------------------------------------------------------------------------
@login_required(login_url="/login/")
def products(request):
    products = models.Product.objects.all()
    context = {'products': products }
    #context = {'segment': 'products'}
    html_template = loader.get_template('home/products.html')
    return HttpResponse(html_template.render(context, request))


@login_required()
def product_detail(request, id):
    product = get_object_or_404(models.Product, id=id)
    context = {'product':product}
    return render(request, 'home/product_detail.html', context)





#------------------------------------------------------------------------------
@login_required(login_url="/login/")
def customers(request):
    customers = models.Customer.objects.all()
    context = {'customers': customers }
    #context = {'segment': 'products'}
    html_template = loader.get_template('home/customers.html')
    return HttpResponse(html_template.render(context, request))


@login_required()
def customer_detail(request, id):
    customer = get_object_or_404(models.Customer, id=id)
    context = {'customer':customer}
    return render(request, 'home/customer_detail.html', context)







#------------------------------------------------------------------------------
@login_required(login_url="/login/")
def order_requests(request):
    reqs = models.Order_request.objects.all()
    context = {'reqs': reqs }
    #context = {'segment': 'products'}
    html_template = loader.get_template('home/order_requests.html')
    return HttpResponse(html_template.render(context, request))


@login_required()
def order_req_detail(request, id):
    req = get_object_or_404(models.Order_request, id=id)
    context = {'req':req}
    return render(request, 'home/order_req_detail.html', context)


























# End
