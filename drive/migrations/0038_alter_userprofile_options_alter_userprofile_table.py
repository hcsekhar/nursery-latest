# Generated by Django 4.2.5 on 2024-02-09 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0037_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'UserProfile'},
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='UserProfile',
        ),
    ]
