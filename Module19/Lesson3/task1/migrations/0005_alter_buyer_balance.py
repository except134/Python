# Generated by Django 5.1.4 on 2024-12-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0004_alter_buyer_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]
