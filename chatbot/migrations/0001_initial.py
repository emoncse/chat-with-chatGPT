# Generated by Django 4.1.7 on 2023-03-29 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl', models.IntegerField(auto_created=True)),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=1000)),
            ],
        ),
    ]
