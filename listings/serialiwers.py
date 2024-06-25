from rest_framework import serializers
from .models import Property, Image, DetailsSection, StepSection, Question, Answer, QuestionChoice, AnswerChoice

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChoice
        fields = '__all__'

class AnswerChoiceSerializer(serializers.ModelSerializer):
    choices = QuestionChoiceSerializer()

    class Meta:
        model = AnswerChoice
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    choices = QuestionChoiceSerializer(many=True, source='questionchoice_set')
    answers = AnswerSerializer(many=True, source='answer_set')

    class Meta:
        model = Question
        fields = '__all__'

class StepSectionSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set')

    class Meta:
        model = StepSection
        fields = '__all__'

class DetailsSectionSerializer(serializers.ModelSerializer):
    steps = StepSectionSerializer(many=True, source='stepsection_set')

    class Meta:
        model = DetailsSection
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, source='image_set')
    details_sections = DetailsSectionSerializer(many=True, source='detailssection_set')

    class Meta:
        model = Property
        fields = '__all__'