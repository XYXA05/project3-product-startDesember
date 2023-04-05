from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy

class Items_buy(models.Model):

    class Meta:
        db_table = 'items_buy'
        verbose_name = 'Телефон который покупаем'
        verbose_name_plural = 'Телефоны которые покупаем'
        
    image_phone = ResizedImageField(size=[100,100], upload_to='for_sell/',verbose_name='Фотография модели телефона')
    model_produkt = models.TextField(max_length=80, verbose_name='Модель продукта ')
    text = models.TextField(max_length=500, verbose_name='Текст')
    max_prise = models.FloatField(verbose_name='Максимальная цена telefoha')
    image_phone_for_buy_bord = ResizedImageField(size=[100,100],upload_to='for_sell/',verbose_name='Фотография модели телефона ha prodazy')


    def __str__(self):
        return self.model_produkt

class Question(models.Model):

    class Meta:
        db_table = 'question'
        verbose_name = 'Вопрос к телефону'
        verbose_name_plural = 'Вопросы к телефону'

 
    items_buy = models.ForeignKey(Items_buy, on_delete=models.RESTRICT)
    titles= models.CharField(max_length=150,verbose_name='Заголовок вопросa')
    question_text =models.TextField(max_length=200, verbose_name='Заголовок вопросa text')

   
    def __str__(self):
           return self.titles


class Choice(models.Model):

    class Meta:
        db_table = 'choice'
        verbose_name = 'Выбор ответа'
        verbose_name_plural = 'Выбор ответов'
    
    question = models.ForeignKey(Question, on_delete=models.RESTRICT,related_name="options")
    title = models.CharField(max_length=1000, verbose_name='Заголовок выбора')
    price_question = models.FloatField(verbose_name='Цена ответа')

    def __str__(self):
        return str(self.price_question)

class Answer(models.Model):
    class Meta:
        db_table = 'answer'
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'

    items_buy = models.ForeignKey(Items_buy, on_delete=models.RESTRICT)
    question = models.ForeignKey(Question, on_delete=models.RESTRICT)
    choice = models.ForeignKey(Choice, on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.items_buy)



def order_validator(order_statys):
    if order_statys not in ['Открыта','Закрыта','Отменена',]:
        raise ValueError(
            gettext_lazy('%(order_statys) Неправильный статус заказа'),
            params = {'order_statys' : order_statys}
        )



class Orders(models.Model):

    class Meta:
        db_table = 'orders_for_sell'
        verbose_name = 'Заказ на продажу'
        verbose_name_plural = 'Заказi на продажi'

    #vitasit vopros i otvet > cyda 
    items_buy = models.ForeignKey(Items_buy,on_delete=models.RESTRICT)
    name = models.CharField(blank=False, null=False, max_length=50, help_text='Ваше имя', verbose_name='Имя продавьца')
    gmail = models.EmailField(blank=False, null=False, help_text='Ваша электронная почта',verbose_name='Почта продавьца')
    phone_nomber = PhoneNumberField(blank=False, null=False, help_text='Ваш номер телефона', verbose_name='Номер телефона продавьца')
    image1 = models.ImageField(blank=False, null=False, help_text='foto nomber1 ', upload_to='for_client/', verbose_name='Фотографии к телефону 1')
    image2 = models.ImageField(blank=False, null=False, help_text='foto nomber2', upload_to='for_client/', verbose_name='Фотографии к телефону 2')
    image3 = models.ImageField(blank=False, null=False, help_text='foto nomber3', upload_to='for_client/', verbose_name='Фотографии к телефону 3')
    image4 = models.ImageField(blank=False, null=False, help_text='foto nomber4', upload_to='for_client/', verbose_name='Фотографии к телефону 4')
    image5 = models.ImageField(blank=False, null=False, help_text='foto nomber5', upload_to='for_client/', verbose_name='Фотографии к телефону 5')
    image6 = models.ImageField(blank=False, null=False, help_text='foto nomber6', upload_to='for_client/', verbose_name='Фотографии к телефону 6')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа на продажу')

    def __str__(self):
        return str(self.items_buy)



class Items_buy_planset(models.Model):

    class Meta:
        db_table = 'items_buy_planset'
        verbose_name = 'Планшет который покупаем'
        verbose_name_plural = 'Планшеты которые покупаем'

    image_planset = ResizedImageField(size=[100,100], upload_to='for_sell/',verbose_name='Фотография модели Планшета')
    model_produkt = models.TextField(max_length=80, verbose_name='Модель продукта ')
    text = models.TextField(max_length=500, verbose_name='Текст')
    max_prise = models.FloatField(verbose_name='Максимальная цена Планшета')
    image_planset_for_buy_bord = ResizedImageField(size=[100,100],upload_to='for_sell/',verbose_name='Фотография модели Планшета ha prodazy')

    def __str__(self):
        return self.model_produkt


class Question_planset(models.Model):

    class Meta:
        db_table = 'question_planset'
        verbose_name = 'Вопрос к Планшетy'
        verbose_name_plural = 'Вопросы к Планшетy'

 
    items_buy_planset = models.ForeignKey(Items_buy_planset, on_delete=models.RESTRICT)
    titles = models.CharField(max_length=150,verbose_name='Заголовок вопросa')
    question_text =models.TextField(max_length=100, verbose_name='Заголовок вопросa text')

    def __str__(self):
           return self.titles



class Choice_planset(models.Model):

    class Meta:
        db_table = 'choice_planset'
        verbose_name = 'Выбор ответа planset'
        verbose_name_plural = 'Выбор ответов planseta'
    
    question_planset = models.ForeignKey(Question_planset, on_delete=models.RESTRICT,related_name="options")
    title = models.CharField(max_length=1000, verbose_name='Заголовок выбора')
    price_question = models.FloatField(verbose_name='Цена ответа')

    def __str__(self):
        return str(self.price_question)


class Answer_planset(models.Model):
    class Meta:
        db_table = 'answer_planset'
        verbose_name = 'Ответ на вопрос planset'
        verbose_name_plural = 'Ответы на вопросы planset'

    items_buy_planset = models.ForeignKey(Items_buy_planset, on_delete=models.RESTRICT)
    question_planset = models.ForeignKey(Question_planset, on_delete=models.RESTRICT)
    choice_planset = models.ForeignKey(Choice_planset, on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.items_buy_planset)


def order_validator(order_statys):
    pass


class Orders_planset(models.Model):

    class Meta:
        db_table = 'orders_for_sell_planset'
        verbose_name = 'Заказ на продажу planset'
        verbose_name_plural = 'Заказi на продажi planset'

    #vitasit vopros i otvet > cyda 
    items_buy_planset = models.ForeignKey(Items_buy_planset,on_delete=models.RESTRICT)
    name = models.CharField(blank=False, null=False, max_length=50, help_text='Ваше имя', verbose_name='Имя продавьца')
    gmail = models.EmailField(blank=False, null=False, help_text='Ваша электронная почта',verbose_name='Почта продавьца')
    phone_nomber = PhoneNumberField(blank=False, null=False, help_text='Ваш номер телефона', verbose_name='Номер телефона продавьца')
    image1 = models.ImageField(blank=False, null=False, help_text='foto nomber1 ', upload_to='for_client/', verbose_name='Фотографии к телефону 1')
    image2 = models.ImageField(blank=False, null=False, help_text='foto nomber2', upload_to='for_client/', verbose_name='Фотографии к телефону 2')
    image3 = models.ImageField(blank=False, null=False, help_text='foto nomber3', upload_to='for_client/', verbose_name='Фотографии к телефону 3')
    image4 = models.ImageField(blank=False, null=False, help_text='foto nomber4', upload_to='for_client/', verbose_name='Фотографии к телефону 4')
    image5 = models.ImageField(blank=False, null=False, help_text='foto nomber5', upload_to='for_client/', verbose_name='Фотографии к телефону 5')
    image6 = models.ImageField(blank=False, null=False, help_text='foto nomber6', upload_to='for_client/', verbose_name='Фотографии к телефону 6')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа на продажу')
    #order_statys = models.TextField(verbose_name='Cтатус заказа',validators=[order_validator])

    def __str__(self):
        return str(self.items_buy_planset)







class Items_buy_watch(models.Model):

    class Meta:
        db_table = 'items_buy_watch'
        verbose_name = 'watch который покупаем'
        verbose_name_plural = 'watches которые покупаем'

    image_watch = ResizedImageField(size=[100,100], upload_to='for_sell/',verbose_name='Фотография модели watch')
    model_produkt = models.TextField(max_length=80, verbose_name='Модель продукта ')
    text = models.TextField(max_length=500, verbose_name='Текст')
    max_prise = models.FloatField(verbose_name='Максимальная цена watch')
    image_watch_for_buy_bord = ResizedImageField(size=[100,100],upload_to='for_sell/',verbose_name='Фотография модели watch ha prodazy')

    def __str__(self):
        return self.model_produkt

class Question_watch(models.Model):

    class Meta:
        db_table = 'question_watch'
        verbose_name = 'Вопрос к Планшетy'
        verbose_name_plural = 'Вопросы к Планшетy'

 
    items_buy_watch = models.ForeignKey(Items_buy_watch, on_delete=models.RESTRICT)
    titles = models.CharField(max_length=150,verbose_name='Заголовок вопросa')
    question_text =models.TextField(max_length=100, verbose_name='Заголовок вопросa text')

    def __str__(self):
           return self.titles


class Choice_watch(models.Model):

    class Meta:
        db_table = 'choice_watch'
        verbose_name = 'Выбор ответа watch'
        verbose_name_plural = 'Выбор ответов watch'
    
    question_watch = models.ForeignKey(Question_watch, on_delete=models.RESTRICT,related_name="options")
    title = models.CharField(max_length=1000, verbose_name='Заголовок выбора')
    price_question = models.FloatField(verbose_name='Цена ответа')

    def __str__(self):
        return str(self.price_question)

class Answer_watch(models.Model):
    class Meta:
        db_table = 'answer_watch'
        verbose_name = 'Ответ на вопрос watch'
        verbose_name_plural = 'Ответы на вопросы watch'

    items_buy_watch = models.ForeignKey(Items_buy_watch, on_delete=models.RESTRICT)
    question_watch = models.ForeignKey(Question_watch, on_delete=models.RESTRICT)
    choice_watch = models.ForeignKey(Choice_watch, on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.items_buy_watch)


def order_validator(order_statys):
    pass


class Orders_watch(models.Model):

    class Meta:
        db_table = 'orders_for_sell_watch'
        verbose_name = 'Заказ на продажу watch'
        verbose_name_plural = 'Заказi на продажi watch'

    #vitasit vopros i otvet > cyda 
    items_buy_watch = models.ForeignKey(Items_buy_watch ,on_delete=models.RESTRICT)
    name = models.CharField(blank=False, null=False, max_length=50, help_text='Ваше имя', verbose_name='Имя продавьца')
    gmail = models.EmailField(blank=False, null=False, help_text='Ваша электронная почта',verbose_name='Почта продавьца')
    phone_nomber = PhoneNumberField(blank=False, null=False, help_text='Ваш номер телефона', verbose_name='Номер телефона продавьца')
    image1 = models.ImageField(blank=False, null=False, help_text='foto nomber1 ', upload_to='for_client/', verbose_name='Фотографии к телефону 1')
    image2 = models.ImageField(blank=False, null=False, help_text='foto nomber2', upload_to='for_client/', verbose_name='Фотографии к телефону 2')
    image3 = models.ImageField(blank=False, null=False, help_text='foto nomber3', upload_to='for_client/', verbose_name='Фотографии к телефону 3')
    image4 = models.ImageField(blank=False, null=False, help_text='foto nomber4', upload_to='for_client/', verbose_name='Фотографии к телефону 4')
    image5 = models.ImageField(blank=False, null=False, help_text='foto nomber5', upload_to='for_client/', verbose_name='Фотографии к телефону 5')
    image6 = models.ImageField(blank=False, null=False, help_text='foto nomber6', upload_to='for_client/', verbose_name='Фотографии к телефону 6')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа на продажу')
    #order_statys = models.TextField(verbose_name='Cтатус заказа',validators=[order_validator])

    def __str__(self):
        return str(self.items_buy_watch)







