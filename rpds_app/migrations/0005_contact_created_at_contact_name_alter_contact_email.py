# Generated by Django 4.0.1 on 2023-05-24 16:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rpds_app', '0004_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
