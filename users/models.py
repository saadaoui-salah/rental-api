from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone



class State(models.Model):
    name = models.CharField(max_length=200)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    BUYER = "BUYER"
    SELLER = "SELLER"
    LOAN_OFFICER = "LOAN_OFFICER"
    REAL_ESTATE_AGENT = "REAL_ESTATE_AGENT"

    USER_CHOICES = [
        (BUYER, 'Buyer'),
        (SELLER, 'Seller'),
        (LOAN_OFFICER, 'Loan Officer'),
        (REAL_ESTATE_AGENT, 'Real Estate Agent'),
    ]

    INTERNAL_SEARCH = "INTERNAL_SEARCH"
    EMAIL_TEXT = "EMAIL/TEXT"
    RADIO = "RADIO"
    TV = "TV"
    OTHER = "OTHER"

    COMING_FROM_CHOICES = [
        (INTERNAL_SEARCH, 'Internal Search'),
        (EMAIL_TEXT, 'Email/Text'),
        (RADIO, 'Radio'),
        (TV, 'TV'),
        (OTHER, 'Other'),
    ]
    
    email = models.EmailField(unique=True)
    user_type = models.CharField(choices=USER_CHOICES, max_length=100)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(max_length=30)
    image = models.ImageField(upload_to="media/users", null=True, blank=True)
    coming_from_choice = models.CharField(max_length=30, choices=COMING_FROM_CHOICES)
    coming_from = models.CharField(max_length=200, null=True, blank=True)
    qualified_with_lender = models.BooleanField(null=True, blank=True)
    lenders_name = models.CharField(max_length=300, null=True, blank=True)
    lenders_contact = models.CharField(max_length=300, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    license_number = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    brokerage_name = models.CharField(max_length=200, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    objects = BaseUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Favorites(models.Model):
    pass