# Generated by Django 2.1.1 on 2018-09-28 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='activity_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.Activity'),
        ),
    ]
