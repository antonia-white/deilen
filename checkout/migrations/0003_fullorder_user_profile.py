# Generated by Django 3.2 on 2022-11-07 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0002_auto_20221102_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullorder',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile'),
        ),
    ]
