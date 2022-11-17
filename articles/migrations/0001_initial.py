# Generated by Django 3.2.13 on 2022-11-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80)),
                ('img', models.CharField(blank=True, max_length=300)),
                ('brand', models.CharField(blank=True, max_length=50)),
                ('connect', models.CharField(blank=True, max_length=50)),
                ('array', models.CharField(blank=True, max_length=50)),
                ('switch', models.CharField(blank=True, max_length=50)),
                ('key_switch', models.CharField(blank=True, max_length=50)),
                ('press', models.IntegerField(blank=True)),
                ('weight', models.CharField(blank=True, max_length=50)),
                ('kind', models.CharField(blank=True, max_length=50)),
                ('bluetooth', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.CharField(max_length=30)),
                ('visit_count', models.IntegerField(default=0)),
            ],
        ),
    ]
