# Generated by Django 3.1.4 on 2021-03-07 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('vname', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('img', models.ImageField(default='', upload_to='mistake/images')),
            ],
        ),
    ]
