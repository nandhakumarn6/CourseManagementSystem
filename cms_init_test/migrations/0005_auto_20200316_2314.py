# Generated by Django 3.0.4 on 2020-03-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_init_test', '0004_auto_20200316_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='lname',
            field=models.CharField(default='00', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default='00'),
        ),
    ]