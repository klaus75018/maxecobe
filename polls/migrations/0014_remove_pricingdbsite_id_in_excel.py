# Generated by Django 5.1.2 on 2024-10-21 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_alter_pricingdbsite_id_in_excel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricingdbsite',
            name='id_in_excel',
        ),
    ]
