# Generated by Django 3.2.4 on 2021-06-09 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_manufaturer_productinfo_manufacturer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='sub_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='imagetype',
            name='product',
        ),
        migrations.AlterField(
            model_name='imagetype',
            name='type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.productinfo'),
        ),
    ]
