# Generated by Django 2.1.2 on 2019-01-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0003_auto_20190108_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
