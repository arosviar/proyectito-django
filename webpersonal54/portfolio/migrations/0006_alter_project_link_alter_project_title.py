# Generated by Django 5.0.6 on 2024-07-11 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Articulo'),
        ),
    ]
