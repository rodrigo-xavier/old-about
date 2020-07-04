# Generated by Django 3.0.7 on 2020-07-04 00:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_auto_20200703_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='from_period',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='From Period'),
        ),
        migrations.AlterField(
            model_name='education',
            name='until_period',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Until Period'),
        ),
    ]