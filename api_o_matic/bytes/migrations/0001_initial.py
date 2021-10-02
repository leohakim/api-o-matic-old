# Generated by Django 3.1.13 on 2021-10-01 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bit',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last modified on')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name of Bit')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description of Bit')),
                ('type_bit', models.CharField(choices=[('string', 'String'), ('number', 'Number'), ('date', 'Date'), ('datetime', 'DateTime')], max_length=50, verbose_name='Type of Bit')),
                ('path', models.CharField(max_length=250, verbose_name='Path of Bit')),
                ('value', models.CharField(blank=True, max_length=250, verbose_name='Value of Bit')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last modified on')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField(verbose_name='URL of Source')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description of Bit')),
                ('type_source', models.CharField(choices=[('html', 'HTML'), ('json', 'JSON')], max_length=50, verbose_name='Type of Source')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Byte',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last modified on')),
                ('slug', models.SlugField(unique=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name of Byte')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Description of Byte')),
                ('public', models.BooleanField(default=True)),
                ('bits', models.ManyToManyField(blank=True, to='bytes.Bit')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bit',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bytes.source'),
        ),
    ]
