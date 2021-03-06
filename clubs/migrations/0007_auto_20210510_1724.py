# Generated by Django 3.2.2 on 2021-05-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_studentprofile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='full_name',
            field=models.CharField(choices=[(1, 'Vasya Pupkin'), (2, 'Dima Zoo'), (3, 'Eugen Nik'), (4, 'Sergey Voo'), (5, 'Илья Знаменский')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo/%Y/%m/%d'),
        ),
    ]
