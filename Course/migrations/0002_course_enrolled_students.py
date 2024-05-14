# Generated by Django 3.2.6 on 2024-05-14 17:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='enrolled_students',
            field=models.ManyToManyField(related_name='enrolled_students', to=settings.AUTH_USER_MODEL),
        ),
    ]