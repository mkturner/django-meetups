# Generated by Django 3.2.11 on 2022-01-27 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meet',
            name='image',
            field=models.ImageField(default=None, upload_to='images'),
            preserve_default=False,
        ),
    ]