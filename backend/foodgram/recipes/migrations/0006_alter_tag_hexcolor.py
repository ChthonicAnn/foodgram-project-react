# Generated by Django 4.2.2 on 2023-06-28 16:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_tag_hexcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='hexcolor',
            field=models.CharField(default='#ffffff', max_length=7, unique=True, validators=[django.core.validators.RegexValidator(message='Введите корректное значение HEX кода цвета', regex='#([a-fA-F0-9]{6})')], verbose_name='Цветовой HEX-код'),
        ),
    ]