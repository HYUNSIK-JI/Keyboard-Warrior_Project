# Generated by Django 3.2.13 on 2022-11-11 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20221111_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyboard',
            name='kind',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]