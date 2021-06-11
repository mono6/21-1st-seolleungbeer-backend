# Generated by Django 3.2.4 on 2021-06-11 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210611_1257'),
        ('orders', '0003_auto_20210609_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(through='orders.OrderItem', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
