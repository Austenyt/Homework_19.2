# Generated by Django 4.2.6 on 2023-10-30 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
