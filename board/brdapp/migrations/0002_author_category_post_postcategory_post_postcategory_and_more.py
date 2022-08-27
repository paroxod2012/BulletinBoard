# Generated by Django 4.1 on 2022-08-19 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brdapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('subscribers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('tank', 'Танки'), ('heal', 'Хилы'), ('dd', 'ДД'), ('buyers', 'Торговцы'), ('guildmaster', 'Галдмастеры'), ('quest', 'Квестгиверы'), ('smith', 'Кузнецы'), ('tanner', 'Кожевники'), ('potion', 'Зельевары'), ('spellmaster', 'Мастера заклинаний')], default='tank', max_length=64)),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brdapp.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brdapp.category')),
                ('postThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brdapp.post')),
            ],
            options={
                'verbose_name': 'Post category',
                'verbose_name_plural': 'Post categories',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='brdapp.PostCategory', to='brdapp.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateCreation', models.DateField(auto_now_add=True)),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brdapp.post')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brdapp.post'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
