# Generated by Django 4.2.3 on 2023-08-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_noticia_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='noticia_imagenes/'),
        ),
    ]
