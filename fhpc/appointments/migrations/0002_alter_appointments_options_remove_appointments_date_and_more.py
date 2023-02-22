# Generated by Django 4.1.7 on 2023-02-20 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_pet_pet_number'),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointments',
            options={'ordering': ['start_time']},
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='date',
        ),
        migrations.AddField(
            model_name='appointments',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointments',
            name='location',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointments',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
