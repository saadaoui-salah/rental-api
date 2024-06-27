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

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        property_instance = Property.objects.create(**validated_data)
        for answer_data in answers_data:
            question_id = answer_data.pop('question')
            question_instance = Question.objects.get(id=question_id)
            Answer.objects.create(question=question_instance, **answer_data)
        return property_instance

    def update(self, instance, validated_data):
        answers_data = validated_data.pop('answers')
        instance.price = validated_data.get('price', instance.price)
        instance.status = validated_data.get('status', instance.status)
        instance.address = validated_data.get('address', instance.address)
        instance.unit_number = validated_data.get('unit_number', instance.unit_number)
        instance.video = validated_data.get('video', instance.video)
        instance.save()

        for answer_data in answers_data:
            question_id = answer_data.pop('question')
            question_instance = Question.objects.get(id=question_id)
            answer_instance, created = Answer.objects.get_or_create(question=question_instance, user=answer_data['user'])
            answer_instance.answer = answer_data.get('answer', answer_instance.answer)
            answer_instance.save()

        return instance