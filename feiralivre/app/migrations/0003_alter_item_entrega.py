# Generated by Django 4.2.3 on 2024-04-19 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_dtentrega_entrega_data_entrega_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='entrega',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='app.entrega'),
        ),
    ]
