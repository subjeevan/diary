# Generated by Django 4.2.2 on 2023-06-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_country_contact_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=40),
        ),
    ]
