# Generated by Django 3.2.2 on 2021-05-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0009_alter_studentprofile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='full_name',
            field=models.IntegerField(choices=[('Vasya Pupkin', 'Vasya Pupkin'), ('Dima Zoo', 'Dima Zoo'), ('Eugen Nik', 'Eugen Nik'), ('Sergey Voo', 'Sergey Voo'), ('Илья Знаменский', 'Илья Знаменский')], max_length=100, null=True),
        ),
    ]
