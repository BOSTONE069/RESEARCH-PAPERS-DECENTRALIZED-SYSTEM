# Generated by Django 4.0.1 on 2023-05-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpds_app', '0006_remove_contact_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]