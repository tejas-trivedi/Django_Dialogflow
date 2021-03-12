# Generated by Django 2.1.5 on 2021-03-12 08:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='statement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Statement'),
        ),
    ]