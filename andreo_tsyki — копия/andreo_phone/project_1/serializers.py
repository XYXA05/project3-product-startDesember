#from rest_framework import serializers
#from .models import Items_buy, Question, Choice, Answer, Orders

#class ChoiceSerializers(serializers.ModelSerializer):
#    defka = serializers.SerializerMethodField()

#    class Meta:
#        model = Choice
#        fields = '__all__'

#    def get_defka(self, obj):
#        total = Answer.objects.filter(Question = obj.Question).count()
#        current = Answer.objects.filter(Question = obj.Question, Choice = obj).count()
#       if total != 0:
#            return float(current * 100 / total)
#       else:
#            return float(0)


#class QuestionSerilaizer(serializers.ModelSerializer):
#    choices  = ChoiceSerializers(many = True, )
#
#    class Meta:
#        model = Question
#        fields = '__all__'

#class AnswerSerilaizer(serializers.ModelSerializer):
#    answers = serializers.JSONField()
#    class Meta:
#        model = Answer
#       fields = '__all__'  

#    def validate_answers(self, answerws):
#       if not answerws:
#            raise serializers.ValidationError('otvet dolboeba')
#        return answerws
    
#    def save(self, pk):
#        answers = self.data['answers']
#        items_buy_id = self.context.items_buy_id 
#        for question_id in answers:
#            question_id = Question.objects.get(pk = question_id)
#            choice = answers[question_id]
#           for choice_id in choice:
#                choice = Choice.objects.get(pk = choice_id)
#                Answer(items_buy_id = items_buy_id, question_id = question_id, choice_id = choice_id).save()
#                items_buy_id.is_answer = True
#                items_buy_id.save()
