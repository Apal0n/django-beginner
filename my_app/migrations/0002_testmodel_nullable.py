# Generated by Django 4.1.7 on 2023-03-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='nullable',
            field=models.TextField(default='Empty text', verbose_name='Какой-то текст'),
            preserve_default=False,
        ),
    ]
