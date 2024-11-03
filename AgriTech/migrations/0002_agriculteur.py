# Generated by Django 5.1.2 on 2024-10-18 22:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgriTech', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agriculteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=15)),
                ('region', models.CharField(max_length=100)),
                ('taille_terres', models.DecimalField(decimal_places=2, help_text='Taille des terres en hectares', max_digits=10)),
                ('type_production', models.CharField(help_text='Type de production agricole (par ex: fruits, légumes, céréales)', max_length=255)),
                ('experience', models.IntegerField(help_text="Nombre d'années d'expérience")),
                ('description', models.TextField(blank=True, help_text="Brève description de l'agriculteur et de son exploitation")),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos_agriculteurs/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agriculteur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]