# Generated by Django 5.1.2 on 2024-10-20 19:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_princingdbprojectsubsubtradegroup_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='POPDBAvailableSusSubTradeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('validation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='POPDBBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('construction_date', models.DateTimeField(verbose_name='Construction Date')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBChosenSusSubTradeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='POPDBProjectPrimInfos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('project_date', models.DateTimeField(verbose_name='Pricings Project Date')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PrincingDBProjectSubPricingSubSubTradeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('group_price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='PrincingDBProjectSubPricingSubTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='princingdbprojectcontainedzone',
            name='project',
        ),
        migrations.RemoveField(
            model_name='princingdbprojectsubsubtrade',
            name='group',
        ),
        migrations.RemoveField(
            model_name='princingdbprojectsubsubtradegroup',
            name='sub_trade',
        ),
        migrations.RemoveField(
            model_name='princingdbprojectsubtrade',
            name='trade',
        ),
        migrations.RemoveField(
            model_name='princingdbprojecttrade',
            name='project',
        ),
        migrations.RemoveField(
            model_name='princingdbprojectpriminfos',
            name='specific_surface',
        ),
        migrations.AddField(
            model_name='princingdbprojectpriminfos',
            name='project_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Project Date'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='POPDBBuildingSurface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.FloatField(default=0.0)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbbuilding')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBContainedSubSubTradeInAvailableGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbavailablesussubtradegroup')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBContainedSubSubTradeInChosenGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbchosensussubtradegroup')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBProjectSubPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('considered_surface', models.FloatField(default=0.0)),
                ('chosen_trade', models.CharField(max_length=200)),
                ('used_index_name', models.CharField(max_length=200)),
                ('index_value_at_pricing_rroject_date', models.FloatField(default=0.0)),
                ('chosen_sub_trade', models.CharField(max_length=200)),
                ('calculated_coeficient', models.FloatField(default=0.0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbprojectpriminfos')),
            ],
        ),
        migrations.AddField(
            model_name='popdbchosensussubtradegroup',
            name='project_sub_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbprojectsubpricing'),
        ),
        migrations.AddField(
            model_name='popdbavailablesussubtradegroup',
            name='project_sub_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbprojectsubpricing'),
        ),
        migrations.CreateModel(
            name='POPDBProjectSubPricingContainedBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_id', models.IntegerField(default=0)),
                ('building_name', models.CharField(max_length=200)),
                ('project_sub_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbprojectsubpricing')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBProjectSubPricingContainedZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_id', models.IntegerField(default=0)),
                ('zone_name', models.CharField(max_length=200)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbprojectsubpricingcontainedbuilding')),
            ],
        ),
        migrations.AddField(
            model_name='popdbprojectpriminfos',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbsite'),
        ),
        migrations.AddField(
            model_name='popdbbuilding',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbsite'),
        ),
        migrations.CreateModel(
            name='POPDBSiteSurface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.FloatField(default=0.0)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbsite')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('classement', models.CharField(max_length=200)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbbuilding')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBHabitationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitation_type', models.CharField(default='', max_length=200)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbzone')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBERTInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(default='', max_length=200)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbzone')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBERPInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erp_type', models.CharField(default='', max_length=200)),
                ('erp_category', models.IntegerField(default='0')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbzone')),
            ],
        ),
        migrations.CreateModel(
            name='POPDBZoneSurface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.FloatField(default=0.0)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.popdbzone')),
            ],
        ),
        migrations.CreateModel(
            name='PrincingDBProjectSubPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('considered_surface', models.FloatField(default=0.0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.princingdbprojectpriminfos')),
            ],
        ),
        migrations.CreateModel(
            name='PrincingDBProjectSubPricingContainedBuilding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_id', models.IntegerField(default=0)),
                ('building_name', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.princingdbprojectsubpricing')),
            ],
        ),
        migrations.CreateModel(
            name='PrincingDBProjectSubPricingContainedZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_id', models.IntegerField(default=0)),
                ('zone_name', models.CharField(max_length=200)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.princingdbprojectsubpricingcontainedbuilding')),
            ],
        ),
        migrations.CreateModel(
            name='PrincingDBProjectSubPricingSubSubTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.princingdbprojectsubpricingsubsubtradegroup')),
            ],
        ),
        migrations.AlterField(
            model_name='princingdbprojectpricedetail',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.princingdbprojectsubpricingsubsubtradegroup'),
        ),
        migrations.CreateModel(
            name='PrincingDBProjectSubPricingSubTradeCompanyOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company_offer_sub_trade_price', models.FloatField(default=0.0)),
                ('sub_trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.princingdbprojectsubpricingsubtrade')),
            ],
        ),
        migrations.AddField(
            model_name='princingdbprojectsubpricingsubsubtradegroup',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.princingdbprojectsubpricingsubtradecompanyoffer'),
        ),
        migrations.CreateModel(
            name='PrincingDBProjectSubPricingTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('used_index_name', models.CharField(max_length=200)),
                ('index_value_at_project_date', models.FloatField(default=0.0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.princingdbprojectsubpricing')),
            ],
        ),
        migrations.AddField(
            model_name='princingdbprojectsubpricingsubtrade',
            name='trade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.princingdbprojectsubpricingtrade'),
        ),
        migrations.DeleteModel(
            name='PrincingDBProjectContainedBuilding',
        ),
        migrations.DeleteModel(
            name='PrincingDBProjectContainedZone',
        ),
        migrations.DeleteModel(
            name='PrincingDBProjectSubSubTrade',
        ),
        migrations.DeleteModel(
            name='PrincingDBProjectSubTrade',
        ),
        migrations.DeleteModel(
            name='PrincingDBProjectTrade',
        ),
        migrations.DeleteModel(
            name='PrincingDBProjectSubSubTradeGroup',
        ),
    ]
