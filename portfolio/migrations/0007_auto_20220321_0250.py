# Generated by Django 3.0.7 on 2022-03-21 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20220321_0249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_date',
            new_name='deadline',
        ),
    ]
