# Generated by Django 3.2.2 on 2021-05-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_auto_20210510_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='full_name',
            field=models.IntegerField(choices=[(1, 'Vasya Pupkin'), (2, 'Dima Zoo'), (3, 'Eugen Nik'), (4, 'Sergey Voo'), (5, 'Илья Знаменский')], max_length=100, null=True),
        ),
    ]
