# Generated by Django 4.2.9 on 2024-02-10 09:09

import carProject.car_owner.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_owner', '0002_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(help_text='Age should be between 18 and 100 years old.', validators=[django.core.validators.MinValueValidator(18, 'Age should be 18 years and above.'), django.core.validators.MaxValueValidator(100, 'Age cannot be more than 100.')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This email is already in use! Provide a new one.'}, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[carProject.car_owner.validators.name_validator]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[carProject.car_owner.validators.name_validator]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=30, validators=[carProject.car_owner.validators.password_validator]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(2, 'Username must be at least 2 chars long!'), carProject.car_owner.validators.char_validator]),
        ),
    ]
