# Generated by Django 4.1.3 on 2022-11-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]
