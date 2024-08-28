# Generated by Django 5.0.7 on 2024-08-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo', models.CharField(choices=[('local', 'Local'), ('internacional', 'Internacional')], max_length=20)),
                ('imagen', models.ImageField(upload_to='productos/')),
            ],
        ),
    ]
