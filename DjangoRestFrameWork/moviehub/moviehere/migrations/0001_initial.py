# Generated by Django 4.1.2 on 2022-10-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('year', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
