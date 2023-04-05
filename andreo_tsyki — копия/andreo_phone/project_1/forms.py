from .models import Items_buy, Answer, Question, Orders, Items_buy_planset, Question_planset, Choice_planset, Answer_planset,Orders_planset
from .models import Items_buy_watch, Question_watch, Choice_watch, Answer_watch, Orders_watch
from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django.db import transaction

class AnswersForm(forms.Form):
    def __init__(self, *args, instance: Items_buy, **kwargs):
        self.instance = instance
        super().__init__(*args, **kwargs)
        questions = Question.objects.filter(items_buy_id=instance)
        existing_answers = {
            question_id: choice_id
            for question_id, choice_id in Answer.objects.filter(
                items_buy=self.instance
            ).values_list("question_id", "choice_id")
        }
        for question in questions:
            self.fields["question_%s" % question.id] = forms.ChoiceField(
                help_text=mark_safe(question.titles),
                label=mark_safe(question.question_text),
                choices=question.options.all().values_list("id", "title"),
                widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
            )
            self.fields["question_%s" % question.id].initial = {} #existing_answers.get(
                #question.id, None
            #) 

    def save(self):
        answers_to_create = []
        for field, value in self.cleaned_data.items():
            if field.startswith("question_"):
                question_id = field.split("_")[-1]
                answers_to_create.append(
                    Answer(
                        items_buy=self.instance,
                        question_id=question_id,
                        choice_id=value,
                    )
                )
        Answer.objects.bulk_create(answers_to_create)
 

class OrdersForm(ModelForm):

    class Meta:
        model = Orders
        fields = ['name','gmail','phone_nomber','image1','image2','image3','image4','image5','image6']






class Answers_planset_Form(forms.Form):
    def __init__(self, *args, instance: Items_buy_planset, **kwargs):
        self.instance = instance
        super().__init__(*args, **kwargs)
        questions = Question_planset.objects.filter(items_buy_planset_id = instance)
        existing_answers = {
            question_planset_id: choice_planset_id
            for question_planset_id, choice_planset_id in Answer_planset.objects.filter(
                items_buy_planset=self.instance
            ).values_list("question_planset_id", "choice_planset_id")
        }
        for question in questions:
            self.fields["question_%s" % question.id] = forms.ChoiceField(
                help_text = mark_safe(question.titles),
                label= mark_safe(question.question_text),
                choices=question.options.all().values_list("id", "title"),   
                widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
            )
            self.fields["question_%s" % question.id].initial = {} #existing_answers.get(
                #question.id, None
            #)

    def save(self): 
        answers_to_create = []
        for field, value in self.cleaned_data.items():
            question_id = field.split("_")[-1]
            answers_to_create.append(
                Answer_planset(
                    items_buy_planset=self.instance,
                    question_id=question_id,
                    choice_id=value,
                )
            )
        Answer_planset.objects.filter(items_buy_planset=self.instance).delete()
        Answer_planset.objects.bulk_create(answers_to_create)   


class Orders_planset_Form(ModelForm):
    #image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Orders_planset
        fields = ['name','gmail','phone_nomber','image1','image2','image3','image4','image5','image6']





class Answers_watch_Form(forms.Form):
    def __init__(self, *args, instance: Items_buy_watch, **kwargs):
        self.instance = instance
        super().__init__(*args, **kwargs)
        questions = Question_watch.objects.filter(items_buy_watch_id = instance)
        existing_answers = {
            question_watch_id: choice_watch_id
            for question_watch_id, choice_watch_id in Answer_watch.objects.filter(
                items_buy_watch=self.instance
            ).values_list("question_watch_id", "choice_watch_id")
        }
        for question in questions:
            self.fields["question_%s" % question.id] = forms.ChoiceField(
                help_text = mark_safe(question.titles),
                label= mark_safe(question.question_text),
                choices=question.options.all().values_list("id", "title"),   
                widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
            )
            self.fields["question_%s" % question.id].initial = {} #existing_answers.get(
                #question.id, None
            #)

    def save(self): 
        answers_to_create = []
        for field, value in self.cleaned_data.items():
            question_id = field.split("_")[-1]
            answers_to_create.append(
                Answer_watch(
                    items_buy_watch=self.instance,
                    question_id=question_id,
                    choice_id=value,
                )
            )
        Answer_watch.objects.filter(items_buy_watch=self.instance).delete()
        Answer_watch.objects.bulk_create(answers_to_create)  

class Orders_watch_Form(ModelForm):
    #image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Orders_watch
        fields = ['name','gmail','phone_nomber','image1','image2','image3','image4','image5','image6']