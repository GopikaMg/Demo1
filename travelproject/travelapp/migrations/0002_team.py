# Generated by Django 4.1.1 on 2023-02-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=250)),
                ('timg', models.ImageField(upload_to='pics')),
                ('tdesc', models.TextField()),
            ],
        ),
    ]
