from django.urls import path
from . import views, views_for_sell
from .admin import shop_admin_site

urlpatterns = [
    path('',views.home, name ='home'),
    path('sell_iphone/', views.sell_iphone, name = 'sell_iphone'),
    path('sell_iphone_page/<int:pk>/', views.sell_iphone_page, name= 'sell_iphone_page'),
    path("getqestionses/<int:pk>/", views.getqestionses, name = 'getqestionses'),
    path('orderforsel/<int:pk>/', views.orderforsel, name = 'orderforsel'),

    path('sell_ipad/', views.sell_planset, name = 'sell_planset'),
    path('sell_ipad_page/<int:pk>/', views.sell_planset_page, name= 'sell_planset_page'),
    path("getqestionses_for_planset/<int:pk>/", views.getqestionses_for_planset, name = 'getqestionses_for_planset'),
    path('orderforsel_planset/<int:pk>/', views.orderforsel_planset, name = 'orderforsel_planset'),

    path('sell_watch/', views.sell_watch, name = 'sell_watch'),
    path('sell_ipad_watch/<int:pk>/', views.sell_watch_page, name= 'sell_watch_page'),
    path("getqestionses_for_watch/<int:pk>/", views.getqestionses_for_watch, name = 'getqestionses_for_watch'),
    path('orderforsel_watch/<int:pk>/', views.orderforsel_watch, name = 'orderforsel_watch'),

    #
    path('home_buy/',views_for_sell.home_buy, name='home_buy' ),


    path('buy_list_phone/', views_for_sell.search_page_phone, name = 'buy_list_phone'),
    path('buy_iphone/<int:pk>/', views_for_sell.buy_iphone, name='buy_iphone'),
    path('zakaz_iphon/<int:pk>/', views_for_sell.ordre_sell_iphone, name='zakaz_iphon'),

    path('buy_list_planset/', views_for_sell.search_page_planset, name='buy_list_planset' ),
    path('buy_planset/<int:pk>/', views_for_sell.buy_planset, name='buy_planset'),
    path('zakaz_planset/<int:pk>/', views_for_sell.ordre_sell_planset, name='zakaz_planset'),

    path('buy_list_watch/', views_for_sell.search_page_watch, name='buy_list_watch'),
    path('buy_watch/<int:pk>/', views_for_sell.buy_watch, name='buy_watch'),
    path('zakaz_watch/<int:pk>', views_for_sell.ordre_sell_watch, name='zakaz_watch'),

    path('home_2/', views_for_sell.home_2, name='home_2'),




    path('pro_has/', views_for_sell.for_as, name='for_as'),
    path('info', views_for_sell.contact, name='contact'),




    path('admin_vikyp/', shop_admin_site.urls)
]
    #path("getqestion/<int:pk>/", views.getqestion.as_view(), name = 'getqestion'),
    #path('results/<int:pk>/', views.results, name = 'orders_for_iphone'),
    #path('vote/<int:pk>/', views.vote, name='vote'),



