# Generated by Django 3.0.8 on 2020-08-25 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appPlatopedia', '0005_auto_20200806_0149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='value_minerals',
            old_name='minerals',
            new_name='fk',
        ),
        migrations.RenameField(
            model_name='value_principalnutriments',
            old_name='principalnutriments',
            new_name='fk',
        ),
        migrations.RenameField(
            model_name='value_vitamins',
            old_name='vitamins',
            new_name='fk',
        ),
    ]
