from django.shortcuts import render, redirect, get_object_or_404
from .models import Items_buy, Question, Choice, Answer, Orders, Items_buy_planset, Question_planset, Choice_planset, Answer_planset, Orders_planset
from .models import Items_buy_watch, Question_watch, Choice_watch, Answer_watch, Orders_watch
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Sum
from .forms import AnswersForm, OrdersForm, Answers_planset_Form, Orders_planset_Form, Answers_watch_Form, Orders_watch_Form
from django.contrib import messages
from .signals import inform_create_order, info_create_planset, info_create_watch

from django.core.mail import send_mail

# Create your views here.
def home(request):

    return render(request, 'home.html')


def sell_iphone(request):
    limit =  request.GET.get('limit')

    if limit == None:
        limit = 40
    limit = int(limit)   

    iphone = Items_buy.objects.filter()
    count = iphone.count()
    page = request.GET.get('page')
    paginator = Paginator(iphone, 1)
    
    try:
        iphone = paginator.page(page)
    except PageNotAnInteger:
        page = 1 
        iphone = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        iphone = paginator.page(page)

    #pages = list(range(1, (paginator.num_pages + 1)))
    iphone = Items_buy.objects.all()
    #iphone = iphone[0:limit]
    context = {'iphone':iphone, 'count':count, 'paginator':paginator, }
    return render(request, 'sell_iphone.html', context)
   


def sell_iphone_page(request,pk ):
    iphones = Items_buy.objects.filter(id=pk)
    context = {'iphones':iphones}
    return render(request, 'sell_iphone_page.html', context)    



def orderforsel( request, pk):
    iphones = get_object_or_404(Items_buy, pk = pk)
    form = OrdersForm(request.POST or None, request.FILES or None)# instance=iphones)
    if form.is_valid():
        order = form.save(commit=False)
        items_buy = Items_buy.objects.get(id=pk)
        order.items_buy = items_buy
        order.save()

        # Send email
        subject = f'Викуп {order.items_buy.model_produkt}'
        message = f'Шановний {order.name},\n\nДякую вам за вашузаявку на викуп смартфону:\n\n{order.items_buy.model_produkt}\n\nС вами звяжиться менеджер в протягом 15-20 хвилин.'
        from_email = 'itao02828@gmail.com' 
        recipient_list = [order.gmail]
        send_mail(subject, message, from_email, recipient_list, inform_create_order)


        return redirect('sell_iphone')
    return render(request, 'orderforsel.html',{'form':form})

from datetime import datetime, timedelta
from django.utils import timezone
def getqestionses(request, pk):
     iphone = get_object_or_404(Items_buy, pk=pk)

     # calculate the time period to consider
     last_count_time = timezone.now() - timedelta(seconds=1)

     # get the total score for the new answers submitted after the last count time
     total_score = 0
     allowed = None  
  

     if request.method == 'POST':
         form = AnswersForm(request.POST, instance=iphone)
         if form.is_valid():
             form.save()
             total_score = iphone.answer_set.filter(
                 created__gt=last_count_time
             ).aggregate(total_score=Sum("choice__price_question"))["total_score"]
             allowed = 'submit'
     else:
         form = AnswersForm(instance=iphone)
         total_score = 0 

     return render(request, "getqestionses.html", {'form': form, 'total_score':total_score, 'iphone':iphone, 'allowed': allowed})



def sell_planset(request):
    limit =  request.GET.get('limit')

    if limit == None:
        limit = 40
    limit = int(limit)   

    planset = Items_buy_planset.objects.filter()
    count = planset.count()
    page = request.GET.get('page')
    paginator = Paginator(planset, 1)
    
    try:
        planset = paginator.page(page)
    except PageNotAnInteger:
        page = 1 
        planset = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        planset = paginator.page(page)

    #pages = list(range(1, (paginator.num_pages + 1)))
    planset = Items_buy_planset.objects.all()
    #iphone = iphone[0:limit]
    context = {'planset':planset, 'count':count, 'paginator':paginator, }
    return render(request, 'sell_planset.html', context)

def sell_planset_page(request,pk ):
    planset = Items_buy_planset.objects.filter(id=pk)
    return render(request, 'sell_planset_page.html', {'planset':planset})

def getqestionses_for_planset(request, pk):
    planset = get_object_or_404(Items_buy_planset, pk = pk)

    last_count_time = timezone.now() - timedelta(seconds=1)

    total_score = 0
    allowed = None

    if request.method == 'POST':
        form = Answers_planset_Form(request.POST, instance=planset)
        if form.is_valid():
            form.save()
            total_score =  total_score = planset.answer_planset_set.filter(
                created__gt=last_count_time
            ).aggregate(total_score=Sum("choice_planset__price_question"))["total_score"]
            allowed = 'submit'
    else:
        form = Answers_planset_Form(instance=planset)
        
    return render(request, "getqestionses_for_planset.html", {"form": form, 'total_score':total_score, 'planset':planset, 'allowed': allowed})


def orderforsel_planset( request, pk):
    planset = get_object_or_404(Items_buy_planset, pk = pk)
    form = Orders_planset_Form(request.POST or None, request.FILES or None)# instance=iphones)
    if form.is_valid():
        order = form.save(commit=False)
        items_buy_planset = Items_buy_planset.objects.get(id=pk)
        order.items_buy_planset = items_buy_planset
        order.save()

        subject = f'Викуп {order.items_buy_planset.model_produkt}'
        message = f'Шановний {order.name},\n\nДякую вам за вашузаявку на викуп:\n\n{order.items_buy_planset.model_produkt}\n\nС вами звяжиться менеджер в протягом 15-20 хвилин.'
        from_email = 'itao02828@gmail.com' 
        recipient_list = [order.gmail]
        send_mail(subject, message, from_email, recipient_list, info_create_planset)

        return redirect('/')
    return render(request, 'orderforsel_planset.html',{'form':form})







def sell_watch(request):
    limit =  request.GET.get('limit')

    if limit == None:
        limit = 40
    limit = int(limit)   

    watch = Items_buy_watch.objects.filter()
    count = watch.count()
    page = request.GET.get('page')
    paginator = Paginator(watch, 1)
    
    try:
        watch = paginator.page(page)
    except PageNotAnInteger:
        page = 1 
        watch = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        watch = paginator.page(page)

    #pages = list(range(1, (paginator.num_pages + 1)))
    watch = Items_buy_watch.objects.all()
    #watch = watch[0:limit]
    context = {'watch':watch, 'count':count, 'paginator':paginator, }
    return render(request, 'sell_watch.html', context)


def sell_watch_page(request,pk ):
    watch = Items_buy_watch.objects.filter(id=pk)
    return render(request, 'sell_watch_page.html', {'watch':watch})

def getqestionses_for_watch(request, pk):
    watch = get_object_or_404(Items_buy_watch, pk = pk)

    last_count_time = timezone.now() - timedelta(seconds=1)

    total_score = 0
    allowed = None

    if request.method == 'POST':
        form = Answers_watch_Form(request.POST, instance = watch)
        if form.is_valid:
            form.save()
            total_score = watch.answer_watch_set.filter(
                created__gt = last_count_time
            ).aggregate(total_score=Sum('choice_watch__price_question'))['total_score']
            allowed = 'submit'
    else:
        form = Answers_planset_Form(instance = watch)
        
    return render(request, "getqestionses_for_watch.html", {"form": form, 'total_score':total_score, 'watch':watch, 'allowed': allowed})


def orderforsel_watch(request, pk):
    watch = get_object_or_404(Items_buy_watch, pk = pk)
    form = Orders_watch_Form(request.POST or None, request.FILES or None)# instance=iphones)
    if form.is_valid():
        order = form.save(commit=False)
        items_buy_watch = Items_buy_watch.objects.get(id=pk)
        order.items_buy_watch = items_buy_watch
        order.save()

        subject = f'Викуп {order.items_buy_watch.model_produkt}'
        message = f'Шановний {order.name},\n\nДякую вам за вашу заявку на викуп годинник:\n\n{order.items_buy_watch.model_produkt}\n\nС вами звяжиться менеджер протягом 15-20 хвилин.'
        from_email = 'itao02828@gmail.com' 
        recipient_list = [order.gmail]
        send_mail(subject, message, from_email, recipient_list, info_create_watch)

        return redirect('/')
    return render(request, 'orderforsel_watch.html',{'form':form})



