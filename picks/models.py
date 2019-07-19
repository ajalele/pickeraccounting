from django.db import models

class Pick(models.Model):
    date_bought = models.DateField(auto_now=False, auto_now_add=False)
    item = models.CharField(max_length=128)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    date_sold = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    profit_loss = models.DecimalField(max_digits=12, decimal_places=2)
    percent_profit = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    speed_of_sale = models.IntegerField(blank=True)
    picture = models.ImageField(upload_to='item_images', blank=True)
    
