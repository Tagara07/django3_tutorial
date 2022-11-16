# Generated by Django 4.1.2 on 2022-11-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0006_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='prince',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(2, '已支付'), (1, '待支付')], default=1, verbose_name='状态'),
        ),
    ]