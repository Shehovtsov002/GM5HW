# Generated by Django 5.0.4 on 2024-05-10 10:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationcode',
            name='confirmation_code',
            field=models.CharField(max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='confirmationcode',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
