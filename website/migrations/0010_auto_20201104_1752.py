# Generated by Django 3.1.2 on 2020-11-04 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0009_auto_20201104_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respostas',
            old_name='data_duv',
            new_name='data_resp',
        ),
        migrations.AlterField(
            model_name='duvida',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
