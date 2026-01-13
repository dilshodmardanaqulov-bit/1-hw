from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Order, OrderItem


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        products = products.filter(category_id=category_id)
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': category_id,
    }
    return render(request, 'store/home.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/detail.html', {'product': product})


def get_cart(request):
    cart = request.session.get('cart', {})
    return cart


def save_cart(request, cart):
    request.session['cart'] = cart


def cart(request):
    cart = get_cart(request)
    cart_items = []
    total = 0
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        total += subtotal
    
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'store/cart.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_cart(request)
    
    product_id_str = str(product_id)
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
    
    save_cart(request, cart)
    messages.success(request, f'{product.name} added to cart!')
    return redirect('cart')


def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        cart = get_cart(request)
        product_id_str = str(product_id)
        
        if quantity > 0:
            cart[product_id_str] = quantity
        else:
            cart.pop(product_id_str, None)
        
        save_cart(request, cart)
    
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = get_cart(request)
    product_id_str = str(product_id)
    cart.pop(product_id_str, None)
    save_cart(request, cart)
    return redirect('cart')


def checkout(request):
    cart = get_cart(request)
    
    if not cart:
        messages.error(request, 'Your cart is empty!')
        return redirect('cart')
    
    cart_items = []
    total = 0
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        total += subtotal
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        if customer_name and phone and address:
            order = Order.objects.create(
                customer_name=customer_name,
                phone=phone,
                address=address,
                total_price=total
            )
            
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['product'].price
                )
            
            request.session['cart'] = {}
            return redirect('success')
        else:
            messages.error(request, 'Please fill in all fields!')
    
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'store/checkout.html', context)


def success(request):
    return render(request, 'store/success.html')
