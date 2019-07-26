from datetime import date
from django import forms
from django.contrib.auth.models import User
from picks.models import Pick, UserProfile


class PickForm(forms.ModelForm):
    date_bought = forms.DateField(widget=forms.SelectDateWidget(), initial=date.today())
    item = forms.CharField(max_length=128)
    purchase_price = forms.DecimalField(max_digits=12, decimal_places=2, initial=0.00)
    date_sold = forms.DateField(widget=forms.HiddenInput(), required=False)
    sale_price = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.HiddenInput(), required=False)
    profit_loss = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.HiddenInput(), required=False)
    percent_profit = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.HiddenInput(), required=False)
    speed_of_sale = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    picture = forms.ImageField(required=False)
    
    class Meta:
        model = Pick
        fields = ('date_bought', 'item', 'purchase_price', 'picture')
        
        
class SoldForm(forms.ModelForm):
    date_bought = forms.DateField(widget=forms.HiddenInput(), required=False)
    item = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False)
    purchase_price = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.HiddenInput(), required=False)
    date_sold = forms.DateField(widget=forms.SelectDateWidget(), initial=date.today())
    sale_price = forms.DecimalField(max_digits=12, decimal_places=2, initial=0.00)
    profit_loss = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.HiddenInput(), required=False)
    percent_profit = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.HiddenInput(), required=False)
    speed_of_sale = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    picture = forms.ImageField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Pick
        fields = ('date_sold', 'sale_price')
        
 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
        
#class UserProfileForm(forms.ModelForm):
    #class Meta:
        #model = UserProfile
        #fields = ('website', 'picture')