# Generated by Django 4.1 on 2022-08-26 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brdapp', '0009_alter_userresponse_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponse',
            name='article',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='brdapp.post'),
        ),
    ]