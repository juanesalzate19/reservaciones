# Generated by Django 4.1.3 on 2022-12-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0010_alter_sillasprofile_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sillasprofile',
            name='fecha',
            field=models.CharField(max_length=50),
        ),
    ]
