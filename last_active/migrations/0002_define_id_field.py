# Generated by Django 2.2.27 on 2022-02-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('last_active', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastactive',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
