from django.shortcuts import render, redirect
from .models import Category,Meal, Logo,Cart, CartItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


def indexpage(request):
    meals = Category.objects.all().filter(bar_food=False,visibility=True)
    bar = Category.objects.all().filter(bar_food=True,visibility=True)
    logo = Logo.objects.all().filter(main=True)
    context = {
        'meals' : meals,
        'bar' : bar,
        'logo':logo
        }
    return render(request, 'baseapp/index.html', context)

def menumeals(request, cat_id):
    cats = Category.objects.get(id=cat_id)
    meals = Meal.objects.filter(category=cats)
    context = {'cat': cats, 'meals': meals}
    return render(request, 'baseapp/menumeal.html', context)

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(meal=meal, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(meal=meal, quantity=1,cart=cart)
        cart.save()
    return redirect('cart')

def cart(request, total=0, quantity=0,cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.meal.price*cart_item.quantity)
            quantity += cart_item.quantity
            allitems = CartItem.objects.all()
    except ObjectDoesNotExist:
        pass

    context = {
        'total' : total,
        'quantity':quantity,
        'cart_items' : cart_items,
        'allitems': allitems 
    }
    return render(request, 'baseapp/cart.html', context)

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        categories = Category.objects.filter(category_name__contains=search)
        searchmeals = Meal.objects.filter(meal_name__contains=search)
        return render(request, 'baseapp/search.html', {'categories':categories,'searchmeals':searchmeals,'search':search})
    else:
        return render(request, 'baseapp/search.html',)