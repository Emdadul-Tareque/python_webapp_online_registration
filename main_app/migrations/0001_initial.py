# Generated by Django 3.0.4 on 2020-03-18 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
