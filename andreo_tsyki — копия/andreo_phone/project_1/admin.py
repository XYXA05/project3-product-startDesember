from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Items_buy, Question, Choice, Answer, Orders, Items_buy_planset, Question_planset, Choice_planset, Answer_planset, Orders_planset
from .models import Items_buy_watch, Question_watch, Choice_watch, Answer_watch, Orders_watch

from.models_for_sell import Phone_Sell, Planset_Sell, Watch_Sell, Photo_Phone_Sell, Photo_Planset_Sell, Photo_Watch_Sell, Order_phone, Order_planset, Order_watch
class ShopAdminSite(AdminSite):
    site_header = 'Shop Administration'
    site_title = 'Shop Admin'
    index_title = 'Welcome to vikyp Admin'

shop_admin_site = ShopAdminSite(name='shop_admin')

class ShopAdmin(admin.ModelAdmin):
    list_display = ('model_produkt', 'text', 'max_prise')
    search_fields = ['model_produkt']
    list_editable = ['max_prise']
    list_per_page = 10

shop_admin_site.register(Items_buy, ShopAdmin)
shop_admin_site.register(Items_buy_planset, ShopAdmin)
shop_admin_site.register(Items_buy_watch, ShopAdmin)


#class QuestionAdmin(admin.ModelAdmin):
#    list_display = ['items_buy', 'titles','question_text']
#    search_fields = ['items_buy__model_produkt', 'titles']
 #   list_editable = ['titles','question_text']
#    list_per_page = 10
#shop_admin_site.register(Question, QuestionAdmin)










class QuestionAdmin(admin.ModelAdmin):
    list_display = ['items_buy', 'titles', 'question_text']
    search_fields = ['items_buy__model_produkt', 'titles']
    list_per_page = 10

    # Define a function to retrieve the related choices
    def get_choices(self, obj):
        return ", ".join([c.title for c in obj.options.all()])

    # Define the columns for the choice information
    get_choices.short_description = 'Choices'
    get_choices.admin_order_field = 'options__title'

    # Combine the ChoiceAdminPhone class into QuestionAdmin
    class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 1
        fields = ['title', 'price_question']

    inlines = [ChoiceInline]
    list_display = ['items_buy', 'titles', 'get_choices']

shop_admin_site.register(Question, QuestionAdmin)



class QuestionPlansetAdmin(admin.ModelAdmin):
    list_display = ['items_buy_planset','titles','question_text']
    search_fields = ['items_buy_planset__model_produkt','titles']
    list_per_page = 10
    
    def get_choices_planset(self, obj):
        return ",".join([c.title for c in obj.options.all()])
    
    get_choices_planset.short_description = 'Choice_planset'
    get_choices_planset.admin_order_field = 'options__title'

    class ChoiceInlinePlanset(admin.TabularInline):
        model = Choice_planset
        extra = 1 
        fields = ['title','price_question']

    inlines = [ChoiceInlinePlanset]
    list_display = ['items_buy_planset', 'titles', 'get_choices_planset']
shop_admin_site.register(Question_planset, QuestionPlansetAdmin)



class QuestionWatchAdmin(admin.ModelAdmin):
    list_display = ['items_buy_watch','titles','question_text']
    search_fields = ['items_buy_watch__model_produkt','titles']
    list_per_page = 10
    
    def get_choices_watch(self, obj):
        return ",".join([c.title for c in obj.options.all()])
    
    get_choices_watch.short_description = 'Choice_watch'
    get_choices_watch.admin_order_field = 'options__title'

    class ChoiceInlineWatch(admin.TabularInline):
        model = Choice_watch
        extra = 1 
        fields = ['title','price_question']

    inlines = [ChoiceInlineWatch]
    list_display = ['items_buy_watch', 'titles', 'get_choices_watch']
shop_admin_site.register(Question_watch, QuestionWatchAdmin)









class AnswerAdminPhone(admin.ModelAdmin):
    list_display = ('items_buy','question','choice','created')
    search_fields = ['items_buy__model_produkt']
    list_per_page = 10
shop_admin_site.register(Answer, AnswerAdminPhone)


class AnswerAdminPlanset(admin.ModelAdmin):
    list_display = ('items_buy_planset','question_planset','choice_planset')
    search_fields = ['items_buy_planset__model_produkt']
    list_per_page = 10
shop_admin_site.register(Answer_planset, AnswerAdminPlanset)


class AnswerAdminWatch(admin.ModelAdmin):
    list_display = ('items_buy_watch','question_watch','choice_watch')
    search_fields = ['items_buy_watch__model_produkt']
    list_per_page = 10
shop_admin_site.register(Answer_watch, AnswerAdminWatch)



class OrdersPhone(admin.ModelAdmin):
    list_display = ['items_buy','name','phone_nomber']
    search_fields = ['items_buy__model_produkt','name']
    list_per_page = 10
shop_admin_site.register(Orders, OrdersPhone)

class OrdersPlanset(admin.ModelAdmin):
    list_display = ['items_buy_planset','name','phone_nomber']
    search_fields = ['items_buy_planset__model_produkt','name']
    list_per_page = 10
shop_admin_site.register(Orders_planset, OrdersPlanset)

class OrdersWatch(admin.ModelAdmin):
    list_display = ['items_buy_watch','name','phone_nomber']
    search_fields = ['items_buy_watch__model_produkt','name']
    list_per_page = 10
shop_admin_site.register(Orders_watch, OrdersWatch)


#######

class SellImageAdmin(admin.StackedInline):
    model = Photo_Phone_Sell

@admin.register(Phone_Sell)
class PostAdmin(admin.ModelAdmin):
    inlines = [SellImageAdmin]
    list_display = ('model', 'price') 

    class Meta:
       model = Phone_Sell


class SellImageAdmin(admin.StackedInline):
    model = Photo_Planset_Sell

@admin.register(Planset_Sell)
class PostAdmin(admin.ModelAdmin):
    inlines = [SellImageAdmin]
    list_display = ('model', 'price') 

    class Meta:
       model = Planset_Sell



class SellImageAdmin(admin.StackedInline):
    model = Photo_Watch_Sell

@admin.register(Watch_Sell)
class PostAdmin(admin.ModelAdmin):
    inlines = [SellImageAdmin]
    list_display = ('model', 'price') 

    class Meta:
       model = Watch_Sell


admin.site.register(Order_phone)
admin.site.register(Order_planset)
admin.site.register(Order_watch)