# Generated by Django 2.2.3 on 2019-09-09 04:59

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import work.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.ImageField(upload_to=work.models.store_project_thumb_image_path)),
                ('description', models.TextField()),
                ('web_link', models.CharField(blank=True, max_length=255, null=True)),
                ('project_type', models.CharField(choices=[('Web Design', 'Web Design'), ('Web Development', 'Web Development'), ('Full Stack', 'Full Stack')], default='Full Stack', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('provided_skill', models.ManyToManyField(to='service.ProvidedSkill')),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='StoreProjectGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('files', models.FileField(upload_to=work.models.store_project_gallery_image_path)),
                ('project_gallery_image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.Store')),
            ],
        ),
        migrations.CreateModel(
            name='StoreProjectFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('files', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Md_Nadir\\Envs\\pythoss\\pythoss\\pythoss\\pythoss_staticfiles_dirs\\prot_media_files'), upload_to=work.models.store_project_file_path)),
                ('free', models.BooleanField(default=False)),
                ('user_required', models.BooleanField(default=True)),
                ('project_file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.Store')),
            ],
        ),
    ]