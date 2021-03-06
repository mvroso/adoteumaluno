# Generated by Django 3.1.2 on 2020-10-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20201029_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arquivo_materiais',
            name='url_arq',
        ),
        migrations.RemoveField(
            model_name='duvida',
            name='url_arq',
        ),
        migrations.RemoveField(
            model_name='respostas',
            name='url_arq',
        ),
        migrations.AddField(
            model_name='arquivo_materiais',
            name='file_mat',
            field=models.FileField(blank=True, null=True, upload_to='uploads/materiais/'),
        ),
        migrations.AddField(
            model_name='duvida',
            name='file_duv',
            field=models.FileField(blank=True, null=True, upload_to='uploads/duvidas/'),
        ),
        migrations.AddField(
            model_name='respostas',
            name='file_res',
            field=models.FileField(blank=True, null=True, upload_to='uploads/duvidas/'),
        ),
    ]
