# Generated by Django 4.2.2 on 2023-06-30 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_rename_tag_recipe_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранное'},
        ),
        migrations.AlterModelOptions(
            name='ingredientinrecipe',
            options={'verbose_name': ('Ингридиент в рецепте',), 'verbose_name_plural': 'Ингридиенты в рецептах'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'verbose_name': 'Список покупок', 'verbose_name_plural': 'Списки покупок'},
        ),
    ]