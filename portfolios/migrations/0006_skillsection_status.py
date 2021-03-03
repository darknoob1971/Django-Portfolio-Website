# Generated by Django 3.1.7 on 2021-03-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0005_skillsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillsection',
            name='status',
            field=models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft')], default='Published', max_length=10),
        ),
    ]
