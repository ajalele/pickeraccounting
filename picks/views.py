from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from picks.forms import PickForm, SoldForm, UserForm
from picks.models import Pick, UserProfile

def index(request):
    user = get_object_or_404(UserProfile, user=request.user)
    picks = user.pick.filter(date_sold__isnull=True)
    return render(request, 'picks/index.html', {'picks': picks})
    
def enter_pick(request):
    form = PickForm()

    if request.method == 'POST':
        form = PickForm(request.POST)

    if form.is_valid():
        scan = form.save(commit=False)
        scan.profit_loss = 0 - scan.purchase_price
        if 'picture' in request.FILES:
            scan.picture = request.FILES['picture']
        scan.save()
        return HttpResponseRedirect('/')
    else:
        print(form.errors)
    return render(request, 'picks/enterpick.html', {'form': form})
    
def sold_pick(request, id):
    instance = get_object_or_404(Pick, id=id)
    instance.date_sold = date.today()

    form = SoldForm(request.POST or None, instance=instance)

    if form.is_valid():
        scan = form.save(commit=False)
        if scan.date_sold < scan.date_bought:
            return render(request, 'picks/soldpick.html', {'form': form, 'pick':instance, 'error': "Sold date must be the same date or a later date than the purchase date"})
            print("Validation Error")
        scan.profit_loss = scan.sale_price - scan.purchase_price
        scan.percent_profit = scan.profit_loss / scan.sale_price
        scan.save()
        return HttpResponseRedirect('/')
    else:
        print(form.errors)
    return render(request, 'picks/soldpick.html', {'form': form, 'pick':instance})
    
def sold_list(request):
    user = get_object_or_404(UserProfile, user=request.user)
    picks = user.pick.filter(date_sold__isnull=False)
    return render(request, 'picks/soldlist.html', {'picks': picks})
    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = UserProfile(user=user)
            profile.save()
            
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        
    return render(request, 'picks/register.html', {'user_form': user_form, 'registered': registered})