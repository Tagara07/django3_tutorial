# Generated by Django 3.2.6 on 2022-10-12 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_userinfo_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='data',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=2),
        ),
    ]
