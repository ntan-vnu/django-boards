# Generated by Django 3.0.1 on 2020-01-02 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='message',
        ),
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='board',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='starter',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='subject',
        ),
    ]
