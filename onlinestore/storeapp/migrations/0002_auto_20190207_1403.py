# Generated by Django 2.1.4 on 2019-02-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderaddress',
            field=models.TextField(),
        ),
    ]
