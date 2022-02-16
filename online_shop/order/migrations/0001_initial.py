# Generated by Django 4.0.2 on 2022-02-16 14:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('total_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total price')),
                ('final_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Final proce')),
                ('status', models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid'), ('C', 'Canceled')], default='U', max_length=1, verbose_name='Order Status')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='customer cart')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(db_index=True, default=False, editable=False)),
                ('count', models.PositiveIntegerField(default=1, help_text='How many Items would you like to order?', validators=[django.core.validators.MinValueValidator(1)], verbose_name='number of Order Items')),
                ('order', models.ForeignKey(help_text='Please select your order', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order', verbose_name='Receipt')),
                ('product', models.ForeignKey(help_text='Please select Product Item to add', on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OffCode',
            fields=[
                ('discount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.discount')),
                ('code', models.CharField(help_text='Please Enter Off code', max_length=10, unique=True, verbose_name='Discount code')),
                ('users', models.ManyToManyField(default=None, help_text='which users have used this code?', null=True, related_name='codes', to='customer.Customer', verbose_name='User Off code')),
            ],
            options={
                'abstract': False,
            },
            bases=('product.discount',),
        ),
    ]
