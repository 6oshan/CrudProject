# Generated by Django 4.2 on 2023-06-08 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='slno',
            field=models.CharField(max_length=250),
        ),
    ]