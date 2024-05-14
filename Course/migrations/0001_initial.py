# Generated by Django 3.2.6 on 2024-05-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.TextField()),
            ],
        ),
    ]