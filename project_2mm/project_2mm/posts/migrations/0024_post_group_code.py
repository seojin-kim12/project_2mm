# Generated by Django 4.2.4 on 2023-08-12 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_userinfo_like_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.group'),
        ),
    ]
