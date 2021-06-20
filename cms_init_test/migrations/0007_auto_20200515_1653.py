# Generated by Django 3.0.4 on 2020-05-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_init_test', '0006_auto_20200316_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='body',
            field=models.TextField(verbose_name="What's on your mind?"),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fname',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='lname',
            field=models.CharField(blank=True, max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True, verbose_name='Phone Number'),
        ),
    ]