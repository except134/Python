# Generated by Django 5.1.4 on 2024-12-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_alter_game_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=1024)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
