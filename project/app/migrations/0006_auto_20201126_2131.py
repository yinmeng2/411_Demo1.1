# Generated by Django 3.1.3 on 2020-11-27 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201126_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='structuredfinancialinvestment',
            name='fp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.financialproduct'),
        ),
        migrations.AlterField(
            model_name='structuredfinancialinvestment',
            name='stock_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.stockinfo'),
        ),
    ]