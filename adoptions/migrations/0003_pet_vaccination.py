# Generated by Django 4.2.4 on 2023-08-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0002_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='vaccination',
            field=models.CharField(default='yes', max_length=50),
        ),
    ]
