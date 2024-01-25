# Generated by Django 4.2.7 on 2023-11-27 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('specialization', '0001_initial'),
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecializationWorkflowMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('specialization_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specialization.specialization')),
                ('workflow_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflow.workflow')),
            ],
        ),
    ]
