# Generated by Django 2.0.13 on 2019-03-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_type', models.CharField(max_length=10)),
            ],
        ),
    ]
