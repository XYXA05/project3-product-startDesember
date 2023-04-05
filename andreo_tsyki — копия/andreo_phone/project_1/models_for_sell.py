from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

class Phone_Sell(models.Model):
    class Meta:
        db_table = 'phone_sell'
        verbose_name = 'Телефон который prodaem'
        verbose_name_plural = 'Телефоны которые prodaem'


    gb = ( ('32gb','32gb'),('64gb','64gb'),('128gb','128gb') )

    image = models.FileField( upload_to='for_buy/')
    price = models.FloatField(verbose_name='price Phone', )
    model = models.TextField(max_length=100, verbose_name='Модель продукта ha prodazy')
    membory = models.TextField(max_length=6, verbose_name='membory for Phone', choices=gb)
    color = models.TextField(verbose_name='color phone')
    stan_telefohy = models.TextField(verbose_name='Стан телефону')
    text = models.TextField( verbose_name='text description for Phone')

    
    def __str__(self):
        return self.model   

class Photo_Phone_Sell(models.Model):
    phone_sell_photo = models.ForeignKey(Phone_Sell, on_delete=models.CASCADE)
    image = models.FileField(upload_to="for_buy/")
    
    

class Order_phone(models.Model):
    class Meta:
        db_table = 'order_phone'
        verbose_name = 'zaiavki ha pokypky telefoha'
        verbose_name_plural = 'zaiavki ha pokypky telefohiv'
    
    phone_sell_product = models.ForeignKey(Phone_Sell, on_delete=models.CASCADE)
    name = models.TextField(max_length=50, verbose_name='ima', blank=False, null=False,)
    famili = models.TextField(max_length=50, blank=False, null=False, verbose_name='familia')
    mail = models.EmailField(blank=False, null=False, verbose_name='posta')
    phone = PhoneNumberField(blank=False, null=False, verbose_name='nomer telefoha')
    sposob_dostavki = models.TextField(verbose_name='sposob_oplati')
    gorod = models.TextField(verbose_name='gorod')
    nomber_viddilehha = models.TextField(verbose_name='nomer_viddilehha')
    sposob_oplati = models.TextField(verbose_name='sposob_oplati')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создания заказа на zakaza')
    
    def __str__(self):
        return self.name    




class Planset_Sell(models.Model):
    class Meta:
        db_table = 'phone_planset'
        verbose_name = 'Planset который prodaem'
        verbose_name_plural = 'Planset которые prodaem'

    image = ResizedImageField(size=[100,100], upload_to='for_buy/')
    price = models.FloatField(verbose_name='price Planset')
    model = models.TextField(max_length=100, verbose_name='Модель продукта ha prodazy')
    membory = models.TextField(max_length=6, verbose_name='membory for Planset')
    color = models.TextField(verbose_name='color phone')
    stan_telefohy = models.TextField(verbose_name='Стан Planset')
    text = models.TextField( verbose_name='text description for Planset')
    
    def __str__(self):
        return self.model

class Photo_Planset_Sell(models.Model):
    planset_sell_photo = models.ForeignKey(Planset_Sell, on_delete=models.CASCADE)
    image = models.FileField(upload_to="for_buy/")

class Order_planset(models.Model):
    class Meta:
        db_table = 'order_planset'
        verbose_name = 'zaiavki ha pokypky planset'
        verbose_name_plural = 'zaiavki ha pokypky planset'
    
    phone_sell_product = models.ForeignKey(Planset_Sell, on_delete=models.CASCADE)
    name = models.TextField(max_length=50, verbose_name='ima', blank=False, null=False,)
    famili = models.TextField(max_length=50, blank=False, null=False, verbose_name='familia')
    mail = models.EmailField(blank=False, null=False, verbose_name='posta')
    phone = PhoneNumberField(blank=False, null=False, verbose_name='nomer planset')
    sposob_dostavki = models.TextField(verbose_name='sposob_oplati')
    gorod = models.TextField(verbose_name='gorod')
    nomber_viddilehha = models.TextField(verbose_name='nomer_viddilehha')
    sposob_oplati = models.TextField(verbose_name='sposob_oplati')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создания заказа на zakaza')
    
    def __str__(self):
        return self.name




class Watch_Sell(models.Model):
    class Meta:
        db_table = 'watch_sell'
        verbose_name = 'watch который pokypaem'
        verbose_name_plural = 'watch которые pakypaem'

    image = ResizedImageField(size=[100,100], upload_to='for_buy/')
    price = models.FloatField(verbose_name='price watch')
    model = models.TextField(max_length=100, verbose_name='Модель продукта ha watch')
    membory = models.TextField(max_length=6, verbose_name='membory for watch')
    color = models.TextField(verbose_name='color watch')
    stan_telefohy = models.TextField(verbose_name='Стан watch')
    text = models.TextField( verbose_name='text description for watch')
    
    def __str__(self):
        return self.model

class Photo_Watch_Sell(models.Model):
    watch_sell_photo = models.ForeignKey(Watch_Sell, on_delete=models.CASCADE)
    image = models.FileField(upload_to="for_buy/")

class Order_watch(models.Model):
    class Meta:
        db_table = 'order_watch'
        verbose_name = 'zaiavki ha pokypky watch'
        verbose_name_plural = 'zaiavki ha pokypky watch'
    
    phone_sell_product = models.ForeignKey(Watch_Sell, on_delete=models.CASCADE)
    name = models.TextField(max_length=50, verbose_name='ima', blank=False, null=False,)
    famili = models.TextField(max_length=50, blank=False, null=False, verbose_name='familia')
    mail = models.EmailField(blank=False, null=False, verbose_name='posta')
    phone = PhoneNumberField(blank=False, null=False, verbose_name='nomer planset')
    sposob_dostavki = models.TextField(verbose_name='sposob_oplati')
    gorod = models.TextField(verbose_name='gorod')
    nomber_viddilehha = models.TextField(verbose_name='nomer_viddilehha')
    sposob_oplati = models.TextField(verbose_name='sposob_oplati')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создания заказа на zakaza')
    
    def __str__(self):
        return self.name