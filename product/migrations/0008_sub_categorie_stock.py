# Generated by Django 3.2.12 on 2022-04-20 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_categorie_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_categorie',
            name='stock',
            field=models.IntegerField(default=10),
        ),
    ]
