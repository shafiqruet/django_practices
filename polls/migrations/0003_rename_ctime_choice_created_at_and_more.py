# Generated by Django 4.1.6 on 2023-02-06 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_ctime_choice_uptime_question_ctime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='ctime',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='uptime',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='ctime',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='uptime',
            new_name='updated_at',
        ),
    ]
