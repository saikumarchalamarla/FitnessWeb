
from .models import GymTip, NutritionTip
from .forms import ContactForm
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .models import Subscription
from django.contrib import messages

def subscriptions(request):
    subs = Subscription.objects.all()
    return render(request, 'gym_nutrition/subscriptions.html', {'subscriptions': subs})

def add_to_cart(request, sub_id):
    subscription = Subscription.objects.get(id=sub_id)
    cart = request.session.get('cart', [])
    cart.append(subscription.id)
    request.session['cart'] = cart
    messages.success(request, f'Added {subscription.plan_name} to cart!')
    return redirect('subscriptions')

def view_cart(request):
    cart = request.session.get('cart', [])
    subscriptions = Subscription.objects.filter(id__in=cart)
    return render(request, 'gym_nutrition/cart.html', {'subscriptions': subscriptions})

def checkout(request):
    cart = request.session.get('cart', [])
    subscriptions = Subscription.objects.filter(id__in=cart)
    if request.method == 'POST':
        # Here you would handle the checkout process (e.g., payment integration)
        request.session['cart'] = []
        messages.success(request, 'Checkout completed!')
        return redirect('home')
    return render(request, 'gym_nutrition/checkout.html', {'subscriptions': subscriptions})

def home(request):
    return render(request, 'gym_nutrition/home.html')

def gym_tips(request):
    tips = GymTip.objects.all()
    return render(request, 'gym_nutrition/gym_tips.html', {'tips': tips})

def nutrition_tips(request):
    tips = NutritionTip.objects.all()
    return render(request, 'gym_nutrition/nutrition_tips.html', {'tips': tips})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact form
            return HttpResponse("Thank you for contacting us!")
    else:
        form = ContactForm()
    return render(request, 'gym_nutrition/contact_us.html', {'form': form})
