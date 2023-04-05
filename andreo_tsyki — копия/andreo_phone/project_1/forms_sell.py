from django import forms
from django.forms import ModelForm
from .models_for_sell import Order_phone, Order_planset, Order_watch
from phonenumber_field.modelfields import PhoneNumberField

class Order_iphone_form(ModelForm):
    MAIL = 'mail'
    DELIVERY = 'delivery'

    CARTA = 'cartoy' 
    HALITSKA = 'halistyka'

    SPOSOB_DOSTAVKI_CHOICES = [
        (MAIL, 'Mail'),
        (DELIVERY, 'Delivery'),
    ]
    SPOSOB_OPLATI_CHOICES = [
        (CARTA, 'cartoy'),
        (HALITSKA, 'halitska'),
    ]
    MAIL_PLACEHOLDER = 'Enter your mail address'
    DELIVERY_PLACEHOLDER = 'Enter your delivery address'
    NAME_PLACEHOLDER = 'write name'
    FAMILI_PLACEHOLDER = 'wasa famolia'
    GOROD_PLACEHOLDER = 'vas gorod'
    NOMBER_VIDDILEHHA = 'nomer vidileha'

    sposob_oplati = forms.ChoiceField(
        label= 'sposob oplatis',
        choices=SPOSOB_OPLATI_CHOICES,
        
    )

    sposob_dostavki = forms.ChoiceField(
        label='Delivery method',
        choices=SPOSOB_DOSTAVKI_CHOICES,
    )
    famili = forms.CharField(label='famili', required=False, widget=forms.TextInput(attrs={'placeholder': FAMILI_PLACEHOLDER}))
    name = forms.CharField(label='name', required=False, widget=forms.TextInput(attrs={'placeholder': NAME_PLACEHOLDER}))
    mail = forms.EmailField(label='Mail address', required=False, widget=forms.EmailInput(attrs={'placeholder': MAIL_PLACEHOLDER}))
    gorod = forms.CharField(label='city', required=False, widget=forms.TextInput(attrs={'placeholder': GOROD_PLACEHOLDER}))
    nomber_viddilehha = forms.CharField(label='nomer viddilehha', required=False, widget=forms.TextInput(attrs={'placeholder': NOMBER_VIDDILEHHA}))
    #sposob_oplati = forms.ChoiceField(label='sposob oplati', required=False, widget=forms.ChoiceField(attrs={'placeholder': sposob_oplati}))
    #gorod = forms.CharField(label='Delivery address', required=False, widget=forms.TextInput(attrs={'placeholder': DELIVERY_PLACEHOLDER}))

    class Meta:
        model = Order_phone
        fields = ['name', 'famili', 'mail', 'phone', 'sposob_dostavki', 'gorod', 'nomber_viddilehha', 'sposob_oplati']




class Order_planset_form(ModelForm):
    MAIL = 'mail'
    DELIVERY = 'delivery'

    CARTA = 'cartoy' 
    HALITSKA = 'halistyka'

    SPOSOB_DOSTAVKI_CHOICES = [
        (MAIL, 'Mail'),
        (DELIVERY, 'Delivery'),
    ]
    SPOSOB_OPLATI_CHOICES = [
        (CARTA, 'cartoy'),
        (HALITSKA, 'halitska'),
    ]
    MAIL_PLACEHOLDER = 'Enter your mail address'
    DELIVERY_PLACEHOLDER = 'Enter your delivery address'
    NAME_PLACEHOLDER = 'write name'
    FAMILI_PLACEHOLDER = 'wasa famolia'
    GOROD_PLACEHOLDER = 'vas gorod'
    NOMBER_VIDDILEHHA = 'nomer vidileha'

    sposob_oplati = forms.ChoiceField(
        label= 'sposob oplatis',
        choices=SPOSOB_OPLATI_CHOICES,
        
    )

    sposob_dostavki = forms.ChoiceField(
        label='Delivery method',
        choices=SPOSOB_DOSTAVKI_CHOICES,
    )
    famili = forms.CharField(label='famili', required=False, widget=forms.TextInput(attrs={'placeholder': FAMILI_PLACEHOLDER}))
    name = forms.CharField(label='name', required=False, widget=forms.TextInput(attrs={'placeholder': NAME_PLACEHOLDER}))
    mail = forms.EmailField(label='Mail address', required=False, widget=forms.EmailInput(attrs={'placeholder': MAIL_PLACEHOLDER}))
    gorod = forms.CharField(label='city', required=False, widget=forms.TextInput(attrs={'placeholder': GOROD_PLACEHOLDER}))
    nomber_viddilehha = forms.CharField(label='nomer viddilehha', required=False, widget=forms.TextInput(attrs={'placeholder': NOMBER_VIDDILEHHA}))
    #sposob_oplati = forms.ChoiceField(label='sposob oplati', required=False, widget=forms.ChoiceField(attrs={'placeholder': sposob_oplati}))
    #gorod = forms.CharField(label='Delivery address', required=False, widget=forms.TextInput(attrs={'placeholder': DELIVERY_PLACEHOLDER}))

    class Meta:
        model = Order_planset
        fields = ['name', 'famili', 'mail', 'phone', 'sposob_dostavki', 'gorod', 'nomber_viddilehha', 'sposob_oplati']





class Order_watch_form(ModelForm):
    MAIL = 'mail'
    DELIVERY = 'delivery'

    CARTA = 'cartoy' 
    HALITSKA = 'halistyka'

    SPOSOB_DOSTAVKI_CHOICES = [
        (MAIL, 'Mail'),
        (DELIVERY, 'Delivery'),
    ]
    SPOSOB_OPLATI_CHOICES = [
        (CARTA, 'cartoy'),
        (HALITSKA, 'halitska'),
    ]
    MAIL_PLACEHOLDER = 'Enter your mail address'
    DELIVERY_PLACEHOLDER = 'Enter your delivery address'
    NAME_PLACEHOLDER = 'write name'
    FAMILI_PLACEHOLDER = 'wasa famolia'
    GOROD_PLACEHOLDER = 'vas gorod'
    NOMBER_VIDDILEHHA = 'nomer vidileha'

    sposob_oplati = forms.ChoiceField(
        label= 'sposob oplatis',
        choices=SPOSOB_OPLATI_CHOICES,
        
    )

    sposob_dostavki = forms.ChoiceField(
        label='Delivery method',
        choices=SPOSOB_DOSTAVKI_CHOICES,
    )
    famili = forms.CharField(label='famili', required=False, widget=forms.TextInput(attrs={'placeholder': FAMILI_PLACEHOLDER}))
    name = forms.CharField(label='name', required=False, widget=forms.TextInput(attrs={'placeholder': NAME_PLACEHOLDER}))
    mail = forms.EmailField(label='Mail address', required=False, widget=forms.EmailInput(attrs={'placeholder': MAIL_PLACEHOLDER}))
    gorod = forms.CharField(label='city', required=False, widget=forms.TextInput(attrs={'placeholder': GOROD_PLACEHOLDER}))
    nomber_viddilehha = forms.CharField(label='nomer viddilehha', required=False, widget=forms.TextInput(attrs={'placeholder': NOMBER_VIDDILEHHA}))
    #sposob_oplati = forms.ChoiceField(label='sposob oplati', required=False, widget=forms.ChoiceField(attrs={'placeholder': sposob_oplati}))
    #gorod = forms.CharField(label='Delivery address', required=False, widget=forms.TextInput(attrs={'placeholder': DELIVERY_PLACEHOLDER}))

    class Meta:
        model = Order_watch
        fields = ['name', 'famili', 'mail', 'phone', 'sposob_dostavki', 'gorod', 'nomber_viddilehha', 'sposob_oplati']