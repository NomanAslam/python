# Generated by Django 5.0.1 on 2024-01-04 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colr', to='api.color'),
        ),
    ]
