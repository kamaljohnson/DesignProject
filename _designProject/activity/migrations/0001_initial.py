# Generated by Django 2.1.1 on 2018-09-22 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('discussion_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='discussions.Discussion')),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOC', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOC', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='idea_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity.Idea'),
        ),
        migrations.AddField(
            model_name='activity',
            name='project_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity.Project'),
        ),
        migrations.AddField(
            model_name='activity',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity.Tag'),
        ),
    ]
