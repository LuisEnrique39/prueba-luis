# Generated by Django 4.2.4 on 2023-09-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacionapp', '0006_remove_tienda_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='pago',
            field=models.BooleanField(default=False, null=True),
        ),
    ]