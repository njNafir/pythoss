# Generated by Django 2.2.3 on 2019-07-31 06:31

from django.db import migrations, models
import django.db.models.deletion
import pss.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=120)),
                ('language_question', models.CharField(max_length=120)),
                ('language_title', models.CharField(max_length=120)),
                ('language_description', models.TextField()),
                ('language_final_text', models.CharField(max_length=120)),
                ('framework_question', models.CharField(max_length=120)),
                ('framework_title', models.CharField(max_length=120)),
                ('framework_description', models.TextField()),
                ('framework_final_text', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='HomeSliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('caption', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to=pss.models.home_slider_image_upload_path)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pss.Info')),
            ],
        ),
    ]
