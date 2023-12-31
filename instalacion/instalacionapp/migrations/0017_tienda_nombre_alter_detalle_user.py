# Generated by Django 4.2.4 on 2023-09-25 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instalacionapp', '0016_remove_producto_comprador'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='nombre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='instalacionapp.producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detalle',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Detalle', to=settings.AUTH_USER_MODEL),
        ),
    ]
