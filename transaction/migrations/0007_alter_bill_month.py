# Generated by Django 4.2.8 on 2023-12-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='month',
            field=models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=20, null=True, verbose_name='Month'),
        ),
    ]
