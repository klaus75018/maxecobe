# Generated by Django 5.1.2 on 2025-01-31 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiecobe', '0006_alter_etude_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etude',
            name='name',
            field=models.CharField(choices=[('Incendie', 'Incendie'), ('Décret Tertiaire', 'Décret Tertiaire'), ('Autre', 'Autre')], max_length=1000),
        ),
    ]
