# Generated by Django 5.0.7 on 2024-07-24 05:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money_control_app', '0007_alter_transaction_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction',
            new_name='MoneyControl',
        ),
    ]