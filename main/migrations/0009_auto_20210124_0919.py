# Generated by Django 3.1.2 on 2021-01-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210124_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='subject',
            field=models.CharField(max_length=64, null=True),
        ),
    ]