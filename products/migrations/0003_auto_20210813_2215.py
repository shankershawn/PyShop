# Generated by Django 2.1.5 on 2021-08-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210813_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default=models.CharField(max_length=150), max_length=500),
        ),
    ]
