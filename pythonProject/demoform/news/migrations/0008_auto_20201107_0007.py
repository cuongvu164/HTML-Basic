# Generated by Django 3.1.3 on 2020-11-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='id',
        ),
        migrations.AlterField(
            model_name='articles',
            name='art_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]