# Generated by Django 4.2.4 on 2023-08-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_ads_owner_alter_ads_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='image',
            field=models.ImageField(default='images.jpg', upload_to='images/ads/'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='type',
            field=models.CharField(choices=[('Хочу научиться', 'Хочу научиться'), ('Могу научить', 'Мoгу научить')], default='Хочу научиться', max_length=100),
        ),
    ]
