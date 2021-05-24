# Generated by Django 3.1.7 on 2021-05-24 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='qualification',
        ),
        migrations.AddField(
            model_name='application',
            name='experiance_in_years',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='qualification',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gmail',
            name='subject',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('teams_present', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.team')),
            ],
        ),
    ]
