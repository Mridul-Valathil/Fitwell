# Generated by Django 3.2.23 on 2024-01-28 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FitWell', '0003_auto_20240128_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestt',
            old_name='requeststate',
            new_name='note',
        ),
        migrations.AddField(
            model_name='requestt',
            name='BATCH',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FitWell.batch'),
        ),
    ]
