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
def products(request):
    products = models.Product.objects.all()
    context = {'products': products }
    #context = {'segment': 'products'}
    html_template = loader.get_template('home/products.html')
    return HttpResponse(html_template.render(context, request))


@login_required()
def product_detail(request, id):
    product = get_object_or_404(models.Product, id=id)
    reqs = models.Order_request.objects.filter(product=product)
    context = {'product':product, 'reqs':reqs}
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
    reqs = models.Order_request.objects.filter(customer=customer)
    context = {'customer':customer, 'reqs':reqs}
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
    req_steps = models.Order_steps.objects.filter(request=req)
    context = {'req':req, 'req_steps':req_steps}
    return render(request, 'home/order_req_detail.html', context)
























# End
