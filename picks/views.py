from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from picks.forms import PickForm

def index(request):
    return render(request, 'picks/index.html')
    
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
        return HttpResponseRedirect('')
    else:
        print(form.errors)
    return render(request, 'picks/enterpick.html', {'form': form})