# Generated by Django 4.1.3 on 2022-11-29 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_responses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskType',
        ),
        migrations.RemoveField(
            model_name='task',
            name='universityTitle',
        ),
        migrations.AddField(
            model_name='category',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.task'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='university', to='api.task'),
            preserve_default=False,
        ),
    ]
