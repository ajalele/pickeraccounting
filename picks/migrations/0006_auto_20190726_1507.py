# Generated by Django 2.2.3 on 2019-07-26 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pick',
            field=models.ManyToManyField(blank=True, null=True, to='picks.Pick'),
        ),
    ]
