from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.contrib.auth.models import User
from .models import Product, Order_request, Customer, Order_incomings
from .forms import TimeForm
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
def etc(request):
    context = {'segment': 'etc'}

    html_template = loader.get_template('home/etc.html')
    return HttpResponse(html_template.render(context, request))






#------------------------------------------------------------------------------
@login_required(login_url="/login/")
def products(request):
    products = models.Product.objects.all().order_by('-date_created')
    context = {'products': products }
    #context = {'segment': 'products'}
    html_template = loader.get_template('home/products.html')
    return HttpResponse(html_template.render(context, request))


@login_required()
def product_detail(request, id):
    product = get_object_or_404(models.Product, id=id)
    reqs = models.Order_request.objects.filter(product=product).order_by('-date_created')
    context = {'product':product, 'reqs':reqs}
    return render(request, 'home/product_detail.html', context)





#------------------------------------------------------------------------------
@login_required(login_url="/login/")
def customers(request):
    customers = models.Customer.objects.all().order_by('-date_created')
    context = {'customers': customers }
    #context = {'segment': 'products'}
    html_template = loader.get_template('home/customers.html')
    return HttpResponse(html_template.render(context, request))


@login_required()
def customer_detail(request, id):
    customer = get_object_or_404(models.Customer, id=id)
    reqs = models.Order_request.objects.filter(customer=customer).order_by('-date_created')
    context = {'customer':customer, 'reqs':reqs}
    return render(request, 'home/customer_detail.html', context)





 

#------------------------------------------------------------------------------
@login_required(login_url="/login/")
def order_requests(request):
    reqs = models.Order_request.objects.all().order_by('-date_created')
    context = {'reqs': reqs }
    #context = {'segment': 'products'}
    html_template = loader.get_template('home/order_requests.html')
    return HttpResponse(html_template.render(context, request))


@login_required()
def order_req_detail(request, id):
    req = get_object_or_404(models.Order_request, id=id)
    incomings = models.Order_incomings.objects.filter(request=req)
    timeform = TimeForm(request.POST)

    if request.method=="POST":
        if timeform.is_valid():
            incoming = Order_incomings()
            incoming.request = req
            incoming.amount = request.POST['amount']
            incoming.save()
            context = {'req':req, 'incomings':incomings, 'timeform':timeform}
            return render(request, 'home/order_req_detail.html', context)

    context = {'req':req, 'incomings':incomings, 'timeform':timeform}
    return render(request, 'home/order_req_detail.html', context)







#------------------------------------------------------------------------------
@login_required(login_url="/login/")
def order_registration(request):
    customers = models.Customer.objects.all().order_by('-date_created')
    products = models.Product.objects.all().order_by('-date_created')
    if request.method=="POST":
        req = Order_request()
        req.user = request.user
        req.customer = get_object_or_404(models.Customer, id=request.POST.get('customer'))
        req.product = get_object_or_404(models.Product, id=request.POST.get('product'))
        req.qty = request.POST['qty']
        req.discount = request.POST['discount']
        req.description = request.POST['description']
        req.save()
        success = 'سفارش جدید ثبت شد'
        context = {'customers': customers , 'products':products, 'success':success}
        return render(request, 'home/order_registration.html', context)

    context = {'customers': customers , 'products':products}
    #context = {'segment': 'products'}
    html_template = loader.get_template('home/order_registration.html')
    return HttpResponse(html_template.render(context, request))





























# End
