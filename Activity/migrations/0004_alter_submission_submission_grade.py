# Generated by Django 3.2.6 on 2024-05-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0003_submission_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_grade',
            field=models.FloatField(default=0.0),
        ),
    ]
