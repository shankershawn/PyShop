# Generated by Django 2.1.5 on 2021-08-13 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210813_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='This is a product', max_length=400),
        ),
    ]
