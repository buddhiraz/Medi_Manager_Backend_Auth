# Generated by Django 4.2.7 on 2024-01-25 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('symptom_master', '0002_alter_symptommaster_symptom_name'),
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultationSymptom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consultation_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='consultation.consultation')),
                ('symptom_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='symptom_master.symptommaster')),
            ],
        ),
    ]
