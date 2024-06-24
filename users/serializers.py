from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = User.objects.filter(email=email).get()
            if not user:
                raise serializers.ValidationError("Invalid credentials")
            user.check_password(password)
        else:
            raise serializers.ValidationError("Both fields are required")

        data['user'] = user
        return data

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        self.token = data['refresh']
        return data

    def save(self, **kwargs):
        RefreshToken(self.token).blacklist()

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):

        if data['user_type'] == CustomUser.BUYER :
            if data['qualified_with_lender'] == None \
            or data['qualified_with_lender'] == "" \
            or data['company'] \
            or data['license_number'] \
            or data['bio'] \
            or data['brokerage_name'] \
            or data['state'] :
                if data['qualified_with_lender'] \
                and not validated_data['lenders_contact'] \
                and not validated_data['lenders_name']:
                    return data
                else:
                    raise serializers.ValidationError("Not Valid Data.")

        if data['user_type'] == CustomUser.SELLER:
            if data['qualified_with_lender'] \
            or data['lenders_name'] \
            or data['lenders_contact'] \
            or data['company'] \
            or data['license_number'] \
            or data['bio'] \
            or data['brokerage_name'] \
            or data['state'] :
                raise serializers.ValidationError("Not Valid Data.")

        elif data['user_type'] == CustomUser.LOAN_OFFICER:
            if data['qualified_with_lender'] \
            or data['lenders_name'] \
            or data['lenders_contact'] \
            or data['brokerage_name'] \
            or not data['company'] \
            or not data['license_number'] \
            or not data['bio'] \
            or data['state'] :
                raise serializers.ValidationError("Not Valid Data.")
        
        elif data['user_type'] == CustomUser.REAL_ESTATE_AGENT:
            if data['qualified_with_lender'] \
            or data['lenders_name'] \
            or data['lenders_contact'] \
            or data['company'] \
            or not data['brokerage_name'] \
            or not data['license_number'] \
            or not data['bio'] \
            or not data['state'] :
                raise serializers.ValidationError("Not Valid Data.")
        
        return data

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            coming_from_choice=validated_data['coming_from_choice'],
            coming_from=validated_data['coming_from'],
            qualified_with_lender=validated_data['qualified_with_lender'],
            lenders_name=validated_data['lenders_name'],
            lenders_contact=validated_data['lenders_contact'],
            company=validated_data['company'],
            license_number=validated_data['license_number'],
            bio=validated_data['bio'],
            brokerage_name=validated_data['brokerage_name'],
            state=validated_data['state'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        return user