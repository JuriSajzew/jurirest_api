# Generated by Django 4.0.6 on 2024-04-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
