# Generated by Django 3.2.10 on 2022-10-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, null=True)),
                ('apellidos', models.CharField(max_length=250, null=True)),
                ('fecha', models.CharField(max_length=250, null=True)),
                ('asunto', models.CharField(max_length=250, null=True)),
                ('correo', models.CharField(max_length=250, null=True)),
                ('comentarios', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
