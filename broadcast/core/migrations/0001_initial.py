# Generated by Django 3.1.2 on 2020-10-09 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=512)),
                ('date', models.DateTimeField(auto_now=True)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Broadcast',
                'verbose_name_plural': 'Broadcasts',
            },
        ),
        migrations.CreateModel(
            name='BroadcastType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=512)),
            ],
            options={
                'verbose_name': 'Broadcast type',
                'verbose_name_plural': 'Broadcast types',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('broadcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.broadcast')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(max_length=512)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('broadcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.broadcast')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.AddField(
            model_name='broadcast',
            name='broadcast_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.broadcasttype'),
        ),
    ]
