# Generated by Django 3.0.1 on 2020-07-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clip', '0008_auto_20200713_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordershop',
            name='email',
            field=models.EmailField(max_length=25, verbose_name='Почта'),
        ),
    ]
