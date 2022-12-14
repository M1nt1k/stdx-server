# Generated by Django 4.1.3 on 2022-11-29 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_task_tasktype_remove_task_universitytitle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='task',
        ),
        migrations.RemoveField(
            model_name='university',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='university',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.university'),
            preserve_default=False,
        ),
    ]
