# Generated by Django 4.0.1 on 2022-07-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('country', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=50)),
                ('addres', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='employee')),
                ('salary', models.FloatField()),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
    ]