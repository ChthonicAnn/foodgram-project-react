# Generated by Django 4.2.2 on 2023-06-30 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_alter_favorite_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredientinrecipe',
            options={'verbose_name': ('Ингредиент в рецепте',), 'verbose_name_plural': 'Ингредиенты в рецептах'},
        ),
    ]