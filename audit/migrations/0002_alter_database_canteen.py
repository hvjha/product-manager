# Generated by Django 4.2.7 on 2024-01-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='Canteen',
            field=models.IntegerField(),
        ),
    ]