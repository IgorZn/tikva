# Generated by Django 3.2.2 on 2021-05-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_studentprofile_student_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='full_name',
            field=models.CharField(choices=[(1, 'Vasya Pupkin'), (2, 'Dima Zoo'), (3, 'Eugen Nik'), (4, 'Sergey Voo')], max_length=100, null=True),
        ),
    ]