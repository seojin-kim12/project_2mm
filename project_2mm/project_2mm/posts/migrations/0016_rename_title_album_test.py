# Generated by Django 4.2.4 on 2023-08-10 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_album_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='title',
            new_name='test',
        ),
    ]
