# Generated by Django 5.2 on 2025-05-04 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_lat', models.FloatField()),
                ('sender_lon', models.FloatField()),
                ('sender_address_text', models.TextField()),
                ('sender_name', models.CharField(max_length=255)),
                ('sender_phone', models.CharField(max_length=20)),
                ('sender_post_code', models.CharField(max_length=20)),
                ('pickup_from_time', models.DateTimeField()),
                ('pickup_to_time', models.DateTimeField()),
                ('recipient_lat', models.FloatField()),
                ('recipient_lon', models.FloatField()),
                ('recipient_address_text', models.TextField()),
                ('recipient_name', models.CharField(max_length=255)),
                ('recipient_phone', models.CharField(max_length=20)),
                ('recipient_post_code', models.CharField(max_length=20)),
                ('delivery_from_time', models.DateTimeField()),
                ('delivery_to_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
