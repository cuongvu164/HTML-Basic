# Generated by Django 3.1.3 on 2020-11-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='art_creat_time',
            new_name='art_create_time',
        ),
        migrations.AlterField(
            model_name='articles',
            name='art_content',
            field=models.TextField(),
        ),
    ]
