# Generated by Django 4.0.5 on 2022-07-05 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_collection_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='project_audio/'),
        ),
    ]
