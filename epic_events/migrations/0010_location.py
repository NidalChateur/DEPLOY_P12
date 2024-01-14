# Generated by Django 5.0 on 2024-01-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epic_events', '0009_alter_contract_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('edition_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nom du lieu')),
                ('number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Numéro')),
                ('street_type', models.CharField(blank=True, choices=[('', ''), ('rue', 'Rue'), ('impasse', 'Impasse'), ('avenue', 'Avenue'), ('boulevard', 'Boulevard'), ('allee', 'Allée'), ('chemin', 'Chemin')], max_length=100, null=True, verbose_name='Type de voie')),
                ('street_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nom de voie')),
                ('city', models.CharField(max_length=100, verbose_name='Ville')),
                ('zip', models.CharField(max_length=6, verbose_name='Code postal')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]