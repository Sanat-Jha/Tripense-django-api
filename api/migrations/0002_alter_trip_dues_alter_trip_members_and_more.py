# Generated by Django 5.1.3 on 2024-12-02 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='dues',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='trip',
            name='members',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='trip',
            name='payments',
            field=models.JSONField(default=list),
        ),
    ]
