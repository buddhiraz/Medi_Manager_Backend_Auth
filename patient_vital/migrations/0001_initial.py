# Generated by Django 4.2.7 on 2024-01-25 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointment', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientVital',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vital_value', models.FloatField(null=True)),
                ('appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appointment.appointment')),
            ],
        ),
    ]