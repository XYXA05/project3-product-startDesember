from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
#from django.urls import reverse
from .models import Orders, Orders_planset, Orders_watch

@receiver (post_save, sender=Orders)
def inform_create_order(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый заказ по {instance.items_buy.model_produkt}'
        message = f"Новый заказ заделан id {instance.id}."#\n\n{reverse('admin:project_1/order/', args=(instance.id,))}
        recipient_list = ['itao02828@gmail.com']
        send_mail(subject, message, 'itao02828@gmail.com', recipient_list)

@receiver (post_save, sender=Orders_planset)
def info_create_planset(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый заказ по {instance.items_buy_planset.model_product}'
        message = f'Новый заказ заделан id {instance.id}.'
        recipient_list = ['itao02828@gmail.com']
        send_mail(subject, message, 'itao02828@gmail.com', recipient_list)

@receiver (post_save, sender=Orders_watch)
def info_create_watch(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый заказ по {instance.items_buy_watch.model_product}'
        message = f'Новый заказ заделан id {instance.id}.'
        recipient_list = ['itao02828@gmail.com']
        send_mail(subject, message, 'itao02828@gmail.com', recipient_list)
