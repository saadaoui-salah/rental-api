# Generated by Django 5.0.6 on 2024-06-27 21:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_question_remove_detailssection_listing_and_more'),
        ('users', '0003_alter_customuser_bio_alter_customuser_brokerage_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('notification_type', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='favorites',
            name='lsiting',
            field=models.ManyToManyField(to='listings.property'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
