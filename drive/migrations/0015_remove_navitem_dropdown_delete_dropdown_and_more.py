# Generated by Django 4.2.5 on 2024-01-29 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0014_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navitem',
            name='dropdown',
        ),
        migrations.DeleteModel(
            name='Dropdown',
        ),
        migrations.DeleteModel(
            name='Navbar',
        ),
        migrations.DeleteModel(
            name='NavItem',
        ),
    ]
