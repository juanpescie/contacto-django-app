# Generated by Django 3.2.5 on 2021-07-26 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('codigo', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('dni', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('X', 'Otro')], default='F', max_length=1)),
                ('fechaNacimiento', models.DateField()),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.persona')),
            ],
        ),
    ]