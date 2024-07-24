# Generated by Django 5.0.7 on 2024-07-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('IN', 'Kirim'), ('OUT', 'Chiqim')], max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account', models.CharField(choices=[('cash', 'Naqd Pul'), ('card', 'Karta'), ('currency', 'Valuta')], max_length=10)),
                ('category', models.CharField(blank=True, choices=[('transport', 'Transport'), ('food', 'Oziq-ovqat'), ('entertainment', "Ko'ngil ochar")], max_length=20, null=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'kirim_chiqim',
            },
        ),
    ]