from django.core.mail import send_mail
from django.shortcuts import render
from .models_for_sell import Phone_Sell, Photo_Phone_Sell, Order_phone, Planset_Sell, Photo_Planset_Sell, Order_planset, Watch_Sell, Photo_Watch_Sell, Order_watch
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import django_filters
from django.db.models.functions import Concat
from django.db.models import Value
from django.shortcuts import render, redirect, get_object_or_404
from .forms_sell import Order_iphone_form, Order_planset_form, Order_watch_form
from django_filters.views import FilterView
from django import forms
from .signals_for_sell import info_create_planset, info_create_watch, inform_create_phone

def home_2(request):
    return render(request, 'home_2.html')

def home_buy(request):
    return render(request, 'home_buy.html')

def for_as(request):
    return render(request, 'for_as.html')

def contact(request):
    return render(request, 'contact.html')

class PhoneFilter(django_filters.FilterSet):

    MODEL_CHOICES = (
        ('iPhone 7', 'iPhone 7'),('iPhone 8', 'iPhone 8'),('iPhone X', 'iPhone X'),
    )

    MEMBORY_CHICES = (
        ('64gb', '64gb'),('128gb', '128gb')
    )

    COLOR_CHOICES = (
        ('black', 'black'),('wite', 'wite')
    )

    STAN_CHOICES = (
        ('dobre', 'dobre'),('pogaho','pogaho')
    )
    
    model = django_filters.ChoiceFilter(choices=MODEL_CHOICES, widget=forms.RadioSelect, empty_label='dalate filter')
    membory = django_filters.ChoiceFilter(choices=MEMBORY_CHICES, widget=forms.RadioSelect, empty_label='dalate filter')
    color = django_filters.ChoiceFilter(choices=COLOR_CHOICES, widget=forms.RadioSelect, empty_label='dalate filter')
    stan_telefohy = django_filters.ChoiceFilter(choices=STAN_CHOICES, widget=forms.RadioSelect, empty_label='dalate filter')

    class Meta:
        model = Phone_Sell
        fields = ['model', 'color', 'membory', 'stan_telefohy']

def search_page_phone(request):
    limit = request.GET.get('limit', 5)
    limit = int(limit) if limit else 5

    queryset = Phone_Sell.objects.all()
    iphone_filter = PhoneFilter(request.GET, queryset=queryset)
    filtered_queryset = iphone_filter.qs

    paginator = Paginator(filtered_queryset, limit)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'iphone': page_obj,
        'count': filtered_queryset.count(),
        'paginator': paginator,
        'filter': iphone_filter,
    }
    return render(request, 'buy_list.html', context)
 


class PhoneFilterView(FilterView):
    model = Phone_Sell
    filterset_class = PhoneFilter
    template_name = 'buy_list.html'


def buy_iphone(request, pk):
    iphone = Phone_Sell.objects.filter(id=pk)
    iphone_photo = Photo_Phone_Sell.objects.filter(phone_sell_photo = pk)
    context = {'iphone':iphone, 'iphone_photo':iphone_photo}
    return render(request, 'buy_iphone.html', context)



def ordre_sell_iphone(request, pk):
    iphone = Phone_Sell.objects.filter(pk = pk)
    form = Order_iphone_form(request.POST or None)
    if form.is_valid():
        order = form.save(commit=False)
        sell_iphhone = Phone_Sell.objects.get(id = pk)
        order.sell_iphone = sell_iphhone
        order.save()

        #send email 
        subject = f'pokypka {order.sell_iphone.model}'
        message = f'sahovhii {order.name},\n\ndakyemo za vasy zaiavky ha\n\n {order.sell_iphone.model}'
        from_email = 'itao02828@gmail.com' 
        recipient_list = [order.mail]
        send_mail = (subject, message, from_email, recipient_list, inform_create_phone)

    context ={'iphone':iphone, 'form':form}
    return render (request, 'zakaz_iphon.html', context)









class PlansetFilter(django_filters.FilterSet):

    MODEL_CHOICES = (
        ('ipad 1', 'ipad 1'),('ipad 8', 'ipad 8'),('ipad', 'ipad'),
    )

    MEMBORY_CHICES = (
        ('64gb', '64gb'),('128gb', '128gb')
    )

    COLOR_CHOICES = (
        ('black', 'black'),('wite', 'wite')
    )

    STAN_CHOICES = (
        ('dobre', 'dobre'),('pogaho','pogaho')
    )
    
    model = django_filters.ChoiceFilter(choices=MODEL_CHOICES, widget=forms.RadioSelect,  empty_label='dalate filter')
    membory = django_filters.ChoiceFilter(choices=MEMBORY_CHICES, widget=forms.RadioSelect, empty_label='dalate filter')
    color = django_filters.ChoiceFilter(choices=COLOR_CHOICES, widget=forms.RadioSelect, empty_label='dalate filter')
    stan_telefohy = django_filters.ChoiceFilter(choices=STAN_CHOICES, widget=forms.RadioSelect, empty_label='dalate filter')

    class Meta:
        model = Planset_Sell
        fields = ['model', 'color', 'membory', 'stan_telefohy']


def search_page_planset(request):
    limit = request.GET.get('limit', 5)
    limit = int(limit) if limit else 5  

    queryset = Planset_Sell.objects.all()
    planset_filter = PlansetFilter(request.GET, queryset = queryset)
    filtered_queryset = planset_filter.qs
    
    paginator = Paginator(filtered_queryset, limit)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'planset':page_obj, 'count':filtered_queryset.count(), 'paginator':paginator, 'filter':planset_filter}
    return render(request, 'buy_list_planset.html', context)


class PlansetFilterView(FilterView):
    model = Planset_Sell
    filterset_class = PlansetFilter
    template_name = 'buy_list_planset.html'


def buy_planset(request, pk):
    planset = Planset_Sell.objects.filter(id=pk)
    planset_photo = Photo_Planset_Sell.objects.filter(phone_sell_photo = pk)
    context = {'planset':planset, 'planset_photo':planset_photo}
    return render(request, 'buy_planset.html', context)

def ordre_sell_planset(request, pk):
    planset = Planset_Sell.objects.filter(pk = pk)
    form = Order_planset_form(request.POST or None)
    if form.is_valid():
        order = form.save(commit=False)
        sell_planset = Planset_Sell.objects.get(id = pk)
        order.sell_planset = sell_planset
        order.save()

        #send email 
        subject = f'pokypka {order.sell_planset.model}'
        message = f'sahovhii {order.name},\n\ndakyemo za vasy zaiavky ha\n\n {order.sell_planset.model}'
        from_email = 'itao02828@gmail.com' 
        recipient_list = [order.mail]
        send_mail = (subject, message, from_email, recipient_list, info_create_planset)

    context = {'planset':planset, 'form':form}
    return render (request, 'zakaz_planset.html', context)















class WatchFilter(django_filters.FilterSet):

    MODEL_CHOICES = (
        ('watch 1', 'watch 1'),('watch 8', 'watch 8'),('watch', 'watch'),
    )

    MEMBORY_CHICES = (
        ('64gb', '64gb'),('128gb', '128gb')
    )

    COLOR_CHOICES = (
        ('black', 'black'),('wite', 'wite')
    )

    STAN_CHOICES = (
        ('dobre', 'dobre'),('pogaho','pogaho')
    )
    
    model = django_filters.ChoiceFilter(choices=MODEL_CHOICES, widget=forms.RadioSelect,  empty_label='dalate filter')
    membory = django_filters.ChoiceFilter(choices=MEMBORY_CHICES, widget=forms.RadioSelect, empty_label='dalate filter')
    color = django_filters.ChoiceFilter(choices=COLOR_CHOICES, widget=forms.RadioSelect, empty_label='dalate filter')
    stan_telefohy = django_filters.ChoiceFilter(choices=STAN_CHOICES, widget=forms.RadioSelect, empty_label='dalate filter')

    class Meta:
        model = Watch_Sell
        fields = ['model', 'color', 'membory', 'stan_telefohy']


def search_page_watch(request):
    limit = request.GET.get('limit', 5)
    limit = int(limit) if limit else 5   

    queryset = Watch_Sell.objects.all()
    watch_filter = WatchFilter(request.GET, queryset = queryset)
    filtered_queryset = watch_filter.qs


    paginator = Paginator(filtered_queryset, limit)
    page_namber = request.GET.get('page')
    page_obj = paginator.get_page(page_namber)

    context = {'watch':page_obj, 'count':filtered_queryset.count(), 'paginator':paginator, 'filter':watch_filter}
    return render(request, 'buy_list_watch.html', context)


class WatchFilterView(FilterView):
    model = Watch_Sell
    filterset_class = WatchFilter
    template_name = 'buy_list_watch.html'


def buy_watch(request, pk):
    watch = Watch_Sell.objects.filter(id=pk)
    watch_photo = Photo_Watch_Sell.objects.filter(phone_sell_photo = pk)
    context = {'watch':watch, 'watch_photo':watch_photo}
    return render(request, 'buy_watch.html', context)

def ordre_sell_watch(request, pk):
    watch = Watch_Sell.objects.filter(pk = pk)
    form = Order_watch_form(request.POST or None)
    if form.is_valid():
        order = form.save(commit=False)
        sell_watch = Watch_Sell.objects.get(id = pk)
        order.sell_watch = sell_watch
        order.save()

        #send email 
        subject = f'pokypka {order.sell_watch.model}'
        message = f'sahovhii {order.name},\n\ndakyemo za vasy zaiavky ha\n\n {order.sell_watch.model}'
        from_email = 'itao02828@gmail.com' 
        recipient_list = [order.mail]
        send_mail = (subject, message, from_email, recipient_list, info_create_watch)

    context = {'watch':watch, 'form':form}
    return render (request, 'zakaz_watch.html', context)