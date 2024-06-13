from django.contrib.auth.models import get_user_model
from rest_framework import serializers
from .models import CustomUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def validate(self, data):

        if data['userType'] == CustomUser.BUYER :
            if data['qualifiedWithLender'] == None \
            or data['qualifiedWithLender'] == "" \
            or data['company'] \
            or data['licenseNumber'] \
            or data['bio'] \
            or data['brokerageName'] \
            or data['state'] :
                if data['qualifiedWithLender'] \
                and not validated_data['lendersContact'] \
                and not validated_data['lendersName']:
                    return data
                else:
                    raise serializers.ValidationError("Not Valid Data.")

        if data['userType'] == CustomUser.SELLER:
            if data['qualifiedWithLender'] \
            or data['lendersName'] \
            or data['lendersContact'] \
            or data['company'] \
            or data['licenseNumber'] \
            or data['bio'] \
            or data['brokerageName'] \
            or data['state'] :
                raise serializers.ValidationError("Not Valid Data.")

        elif data['userType'] == CustomUser.LOAN_OFFICER:
            if data['qualifiedWithLender'] \
            or data['lendersName'] \
            or data['lendersContact'] \
            or data['brokerageName'] \
            or not data['company'] \
            or not data['licenseNumber'] \
            or not data['bio'] \
            or data['state'] :
                raise serializers.ValidationError("Not Valid Data.")
        
        elif data['userType'] == CustomUser.REAL_ESTATE_AGENT:
            if data['qualifiedWithLender'] \
            or data['lendersName'] \
            or data['lendersContact'] \
            or data['company'] \
            or not data['brokerageName'] \
            or not data['licenseNumber'] \
            or not data['bio'] \
            or not data['state'] :
                raise serializers.ValidationError("Not Valid Data.")
        
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            phone_number=validated_data['phoneNumber']
            image=validated_data['image']
            coming_from_choice=validated_data['comingFromChoice']
            coming_from=validated_data['coming_from']
            qualified_with_lender=validated_data['qualifiedWithLender']
            lenders_name=validated_data['lendersName']
            lenders_contact=validated_data['lendersContact']
            company=validated_data['company']
            license_number=validated_data['licenseNumber']
            bio=validated_data['bio']
            brokerage_name=validated_data['brokerageName']
            state=validated_data['state'],
            image=validated_data['image'],
            user_type=validated_data['userType']
        )
        return user