# Generated by Django 5.0.6 on 2024-06-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/users'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='qualified_with_lender',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
