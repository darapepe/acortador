# Generated by Django 2.2 on 2022-11-10 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('codigo', models.CharField(blank=True, max_length=8)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('contador', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Enlaces',
            },
        ),
    ]
