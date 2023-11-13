# Generated by Django 4.2.7 on 2023-11-13 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('main', '0002_rename_empployee_order_employee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.client', verbose_name='client'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='quantity available'),
        ),
    ]