# Generated by Django 2.2 on 2020-02-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20200126_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=6),
        ),
    ]