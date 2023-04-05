from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
#from django.urls import reverse
from .models_for_sell import Order_phone, Order_planset, Order_watch

@receiver (post_save, sender=Order_phone)
def inform_create_phone(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый pokypka по {instance.phone_sell_product.model}'
        message = f"Новый заказ заделан id {instance.id}."#\n\n{reverse('admin:project_1/order/', args=(instance.id,))}
        recipient_list = ['itao02828@gmail.com']
        send_mail(subject, message, 'itao02828@gmail.com', recipient_list)

@receiver (post_save, sender=Order_planset)
def info_create_planset(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый pokypka по {instance.phone_sell_product.model_product}'
        message = f'Новый заказ заделан id {instance.id}.'
        recipient_list = ['itao02828@gmail.com']
        send_mail(subject, message, 'itao02828@gmail.com', recipient_list)

@receiver (post_save, sender=Order_watch)
def info_create_watch(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый pokypka по {instance.phone_sell_product.model_product}'
        message = f'Новый заказ заделан id {instance.id}.'
        recipient_list = ['itao02828@gmail.com']
        send_mail(subject, message, 'itao02828@gmail.com', recipient_list)