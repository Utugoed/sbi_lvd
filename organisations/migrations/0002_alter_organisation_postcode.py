# Generated by Django 3.2 on 2023-06-05 10:26

from django.db import migrations, models
import organisations.models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='postcode',
            field=models.IntegerField(validators=[organisations.models.validate_postcode]),
        ),
    ]