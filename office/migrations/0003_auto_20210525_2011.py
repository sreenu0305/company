# Generated by Django 3.1.7 on 2021-05-25 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0002_auto_20210524_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='team',
        ),
        migrations.RemoveField(
            model_name='project',
            name='teams_present',
        ),
        migrations.AddField(
            model_name='team',
            name='project_working',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='office.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gmail',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.employee'),
        ),
        migrations.AlterField(
            model_name='gmail',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_lead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.employee'),
        ),
    ]
