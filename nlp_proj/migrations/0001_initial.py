# Generated by Django 3.1.7 on 2021-03-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.IntegerField(default=0)),
                ('text', models.TextField(default='')),
                ('label', models.IntegerField()),
            ],
        ),
    ]