# Generated by Django 5.0 on 2023-12-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_management_app', '0002_alter_purchaseorder_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='items',
            field=models.TextField(),
        ),
    ]
