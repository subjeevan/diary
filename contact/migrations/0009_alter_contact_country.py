# Generated by Django 4.2.2 on 2023-06-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_alter_contact_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.JSONField(blank=True, null=True),
        ),
    ]