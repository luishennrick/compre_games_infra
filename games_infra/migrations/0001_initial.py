# Generated by Django 3.2.17 on 2023-02-13 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('score', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]
