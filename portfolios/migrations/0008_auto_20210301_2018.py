# Generated by Django 3.1.7 on 2021-03-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0007_enablesections'),
    ]

    operations = [
        migrations.AddField(
            model_name='enablesections',
            name='footer',
            field=models.CharField(choices=[('Show', 'Show'), ('Hide', 'Hide')], default='Show', max_length=5),
        ),
        migrations.AddField(
            model_name='enablesections',
            name='header',
            field=models.CharField(choices=[('Show', 'Show'), ('Hide', 'Hide')], default='Shwo', max_length=5),
        ),
    ]
