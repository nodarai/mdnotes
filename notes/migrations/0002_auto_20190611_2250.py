# Generated by Django 2.2.2 on 2019-06-11 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
