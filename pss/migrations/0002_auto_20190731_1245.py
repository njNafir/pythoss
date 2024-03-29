# Generated by Django 2.2.3 on 2019-07-31 06:45

from django.db import migrations, models
import pss.models


class Migration(migrations.Migration):

    dependencies = [
        ('pss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='framework_background_image',
            field=models.ImageField(default='Whoof', upload_to=pss.models.bg_image_upload_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='language_background_image',
            field=models.ImageField(default='WHoff', upload_to=pss.models.bg_image_upload_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homesliderimage',
            name='caption',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='homesliderimage',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
