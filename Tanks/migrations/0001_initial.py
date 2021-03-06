# Generated by Django 2.2.5 on 2021-02-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('country', models.CharField(default='-', max_length=120)),
                ('generation', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th')], max_length=120)),
                ('year', models.IntegerField(default=0)),
                ('weight', models.TextField(default='-')),
                ('crew', models.CharField(default='-', max_length=120)),
                ('main_armament', models.TextField(default='-')),
                ('rounds', models.IntegerField(default=0)),
                ('autoloader', models.BooleanField(default=False)),
                ('secondary_armaments', models.TextField(default='-')),
                ('remote_weapons_system', models.BooleanField(default=False)),
                ('active_protection_system', models.BooleanField(default=False)),
                ('engine', models.TextField(default='-')),
                ('power_to_weight_ratio', models.CharField(default='-', max_length=120)),
                ('transmission', models.TextField(default='-')),
                ('suspension', models.TextField(default='-')),
                ('maximum_speed', models.TextField(default='-')),
                ('range', models.CharField(default='-', max_length=120)),
                ('length', models.CharField(default='-', max_length=120)),
                ('width', models.CharField(default='-', max_length=120)),
                ('height', models.CharField(default='-', max_length=120)),
            ],
        ),
    ]
