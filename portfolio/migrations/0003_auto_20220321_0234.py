# Generated by Django 3.0.7 on 2022-03-21 02:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_manager_meeting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='purchase_date',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='purchase_price',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='shares',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='symbol',
        ),
        migrations.AddField(
            model_name='manager',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='manager',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='manager',
            name='email',
            field=models.EmailField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='manager',
            name='manager_number',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='manager',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='manager',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='meeting',
            name='manager',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='meetings_m', to='portfolio.Manager'),
        ),
    ]
