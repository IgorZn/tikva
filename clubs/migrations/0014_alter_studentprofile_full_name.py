# Generated by Django 3.2.2 on 2021-05-10 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0013_alter_studentprofile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='full_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='full_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
