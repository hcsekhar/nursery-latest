# Generated by Django 4.2.5 on 2024-02-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0048_alter_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField(default=0)),
                ('Brand_name', models.CharField(max_length=1000)),
                ('message', models.TextField(max_length=10000)),
            ],
        ),
    ]
