# Generated by Django 4.1 on 2022-08-24 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brdapp', '0004_remove_category_subscribers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userresponse',
            options={'ordering': ['-create']},
        ),
        migrations.RenameField(
            model_name='userresponse',
            old_name='dateCreation',
            new_name='create',
        ),
    ]
