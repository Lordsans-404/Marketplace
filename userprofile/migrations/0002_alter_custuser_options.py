# Generated by Django 3.2 on 2023-04-27 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custuser',
            options={'ordering': ['username', 'email', 'first_name', 'last_name', 'avatar', 'about']},
        ),
    ]