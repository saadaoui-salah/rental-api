# Generated by Django 5.0.6 on 2024-06-13 18:39

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_type', models.CharField(choices=[('BUYER', 'Buyer'), ('SELLER', 'Seller'), ('LOAN_OFFICER', 'Loan Officer'), ('REAL_ESTATE_AGENT', 'Real Estate Agent')], max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=30)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='media/users')),
                ('coming_from_choice', models.CharField(choices=[('INTERNAL_SEARCH', 'Internal Search'), ('EMAIL/TEXT', 'Email/Text'), ('RADIO', 'Radio'), ('TV', 'TV'), ('OTHER', 'Other')], max_length=30)),
                ('coming_from', models.CharField(max_length=200)),
                ('qualified_with_lender', models.BooleanField(default=False)),
                ('lenders_name', models.CharField(max_length=300)),
                ('lenders_contact', models.CharField(max_length=300)),
                ('company', models.CharField(max_length=200)),
                ('license_number', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('brokerage_name', models.CharField(max_length=200)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.state')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
