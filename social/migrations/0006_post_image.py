# Generated by Django 3.2.8 on 2021-11-11 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20211106_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/post_photos'),
        ),
    ]
