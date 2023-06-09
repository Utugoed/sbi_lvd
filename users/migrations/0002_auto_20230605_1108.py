# Generated by Django 3.2 on 2023-06-05 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0003_alter_organisation_options'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'default_related_name': 'users'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='organisation',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='organisations.organisation'),
        ),
    ]
