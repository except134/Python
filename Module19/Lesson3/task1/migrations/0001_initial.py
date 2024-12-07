# Generated by Django 5.1.4 on 2024-12-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('age_limited', models.BooleanField(default=False)),
                ('buyer', models.ManyToManyField(to='task1.buyer')),
            ],
        ),
    ]
