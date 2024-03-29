# Generated by Django 4.2.7 on 2024-01-31 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('procedure', '0001_initial'),
        ('specialization', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSpecializationProcedureMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('procedure_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='procedure.procedure')),
                ('specialization_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='specialization.specialization')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
