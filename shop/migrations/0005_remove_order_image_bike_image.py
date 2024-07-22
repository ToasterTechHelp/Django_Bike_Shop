# Generated by Django 4.1.1 on 2024-07-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_order_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
        migrations.AddField(
            model_name='bike',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
