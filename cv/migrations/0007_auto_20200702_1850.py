# Generated by Django 3.0.7 on 2020-07-02 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_auto_20200702_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='born',
            new_name='birth',
        ),
    ]
