# Generated by Django 4.1 on 2022-08-25 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brdapp', '0006_alter_userresponse_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userresponse',
            options={'ordering': ['-creation']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='create',
        ),
        migrations.AddField(
            model_name='userresponse',
            name='creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
