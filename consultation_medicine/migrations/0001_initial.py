# Generated by Django 4.2.7 on 2024-01-31 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicine_master', '0002_rename_medicine_master_medicinemaster'),
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultationMedicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('medicine_dosage', models.DecimalField(decimal_places=1, default=1.0, max_digits=2)),
                ('medicine_timing', models.CharField(choices=[('MN', 'MORNING'), ('MD', 'MIDDAY'), ('NN', 'NOON'), ('AF', 'AFTERNOON'), ('EV', 'EVENING'), ('NT', 'NIGHT')], default='MN', max_length=2)),
                ('medicine_timing_food', models.CharField(choices=[('AF', 'AFTER_FOOD'), ('BF', 'BEFORE_FOOD')], default='AF', max_length=2)),
                ('instruction', models.TextField(blank=True, max_length=200)),
                ('consultation_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='consultation.consultation')),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicine_master.medicinemaster')),
            ],
        ),
    ]
