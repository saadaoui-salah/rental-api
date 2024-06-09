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

    COMING_FROM_CHOICES = [
        ("INTERNAL_SEARCH", 'Internal Search'),
        ("EMAIL/TEXT", 'Email/Text'),
        ("RADIO", 'Radio'),
        ("TV", 'TV'),
        ("OTHER", 'Other'),
    ]
    
    email = models.EmailField(unique=True)
    user_type = models.CharField(choices=USER_CHOICES, max_length=100)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="/media/users")
    coming_from_choice = models.CharField(max_length=30, choices=COMING_FROM_CHOICES)
    coming_from = models.CharField(max_length=200)
    qualified_with_lender = models.BooleanField(default=False)
    lenders_name = models.CharField(max_length=300)
    lenders_contact = models.CharField(max_length=300)
    company = models.CharField(max_length=200)
    license_number = models.CharField(max_length=200)
    bio = models.TextField()
    brokerage_name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    objects = BaseUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Favorites(models.Model):
    pass