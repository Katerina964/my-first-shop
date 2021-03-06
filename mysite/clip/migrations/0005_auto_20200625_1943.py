# Generated by Django 3.0.1 on 2020-06-25 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clip', '0004_auto_20200619_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordershop',
            name='choice',
        ),
        migrations.AlterField(
            model_name='ordershop',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='ordershop',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='ordershop',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='ordershop',
            name='surname',
            field=models.CharField(max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='ordershop',
            name='town',
            field=models.CharField(max_length=20, verbose_name='Город'),
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='hairclip', verbose_name='photo')),
                ('title', models.CharField(max_length=100)),
                ('price', models.PositiveSmallIntegerField()),
                ('quantity', models.PositiveSmallIntegerField()),
                ('ordershop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clip.Ordershop')),
            ],
        ),
    ]
