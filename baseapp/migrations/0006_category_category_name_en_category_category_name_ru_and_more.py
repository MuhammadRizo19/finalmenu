# Generated by Django 4.2 on 2023-05-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0005_cart_alter_meal_meal_image2_alter_meal_meal_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name_en',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_name_en',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_name_ru',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='section_name_en',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='section_name_ru',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
