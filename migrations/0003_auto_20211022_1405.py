# Generated by Django 3.2.4 on 2021-10-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selling_app', '0002_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizer',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='fertilizer',
            name='weight',
            field=models.CharField(max_length=1000),
        ),
    ]
