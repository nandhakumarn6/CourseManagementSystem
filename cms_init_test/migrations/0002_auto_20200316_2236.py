# Generated by Django 2.2.6 on 2020-03-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_init_test', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AlterField(
            model_name='contact',
            name='body',
            field=models.TextField(),
        ),
    ]