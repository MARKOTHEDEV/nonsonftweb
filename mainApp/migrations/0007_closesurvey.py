# Generated by Django 4.0.4 on 2022-05-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_survey_discordid'),
    ]

    operations = [
        migrations.CreateModel(
            name='closeSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isOpen', models.BooleanField(default=False)),
            ],
        ),
    ]