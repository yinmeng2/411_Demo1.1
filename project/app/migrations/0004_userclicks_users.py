# Generated by Django 3.0.5 on 2020-11-27 04:22

from django.db import migrations, models
import django.db.models.manager
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_financialproduct_structuredfinancialinvestment'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserClicks',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('stock_id', models.IntegerField(default=0)),
                ('user_id', models.CharField(max_length=255)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('use_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('user_details', djongo.models.fields.JSONField()),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
