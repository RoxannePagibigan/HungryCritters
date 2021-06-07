from django.db.models.query import EmptyQuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from login.models import User

def indexHome(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "home.html", context)

def viewProduct(request, product_id):
    view_products = Product.objects.get(id=product_id)
    context = {
        'view_products': view_products
    }
    return render(request, "products.html", context)


def viewCart(request):
    try:
        this_user = User.objects.get(id=request.session['user_id'])
        add_cart = Order.objects.get(customer = this_user, complete = False)
        orderitems = OrderItem.objects.all()

        context = {
            "add_cart": add_cart,
            "orderitems": orderitems,
            }
        
        return render(request, "cart.html", context)
    except:
        add_cart = {}

        return render(request, "cart.html")

def viewCheckout(request):
    this_user = User.objects.get(id=request.session['user_id'])
    add_cart = Order.objects.get(customer = this_user, complete = False)
    orderitems = OrderItem.objects.all()

    context = {
        "add_cart": add_cart,
        "orderitems": orderitems
    }
    return render(request, "checkout.html", context)

def addToCart(request, product_id):
    this_user = User.objects.get(id=request.session['user_id'])
    add_product = Product.objects.get(id=product_id)

    if request.method == "POST":
        
        order, created = Order.objects.get_or_create(customer = this_user, complete = False)
        orderitem, created = OrderItem.objects.get_or_create(order = order, product = add_product)
        
        orderitem.quantity += 1
        orderitem.subtotal = add_product.price * orderitem.quantity
        orderitem.save()
        order.total += float(orderitem.subtotal)
        order.items += 1
        order.save()
        
    return redirect(f'/product/{product_id}')

def addItem(request, id):
    this_user = User.objects.get(id=request.session['user_id'])
    ordercart = Order.objects.get(customer = this_user, complete = False)
    itemorder = OrderItem.objects.get(id=id)

    itemorder.quantity += 1
    itemorder.subtotal += itemorder.product.price
    itemorder.save()
    ordercart.total += float(itemorder.product.price)
    ordercart.items += 1
    ordercart.save()
    return redirect("/cart")

def removeItem(request, id):
    this_user = User.objects.get(id=request.session['user_id'])
    ordercart = Order.objects.get(customer = this_user, complete = False)
    itemorder = OrderItem.objects.get(id=id)

    itemorder.quantity -= 1
    itemorder.subtotal -= itemorder.product.price
    itemorder.save()
    ordercart.total -= float(itemorder.product.price)
    ordercart.items -= 1
    ordercart.save()

    if itemorder.quantity == 0:
        itemorder.delete()
    return redirect("/cart")

def processOrder(request, id):
    this_user = User.objects.get(id=request.session['user_id'])
    add_cart = Order.objects.get(id=id)

    if request.method == "POST":
        shipping = Shipping.objects.create(
            customer=this_user,
            order=add_cart,
            address = request.POST['address'],
            city = request.POST['city'],
            state = request.POST['state'],
            zipcode = request.POST['zipcode']
            )

    add_cart.complete = True
    add_cart.save()
    return redirect('/home')