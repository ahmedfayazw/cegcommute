# Generated by Django 3.2.12 on 2022-03-21 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Branch', models.CharField(max_length=100)),
                ('Stream', models.CharField(max_length=10)),
                ('RollNumber', models.CharField(max_length=10)),
                ('Campus', models.CharField(max_length=3)),
                ('BloodGroup', models.CharField(max_length=7)),
                ('PhoneNumber', models.CharField(max_length=13)),
                ('Address', models.CharField(max_length=255)),
                ('ReferenceID', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('ValidUntil', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.CharField(choices=[('Arumbakkam', 'Arumbakkam'), ('', '')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.CharField(choices=[('Arumbakkam', 'Arumbakkam'), ('', '')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleNumber', models.CharField(max_length=10)),
                ('VehicleType', models.CharField(choices=[('Car', 'Car'), ('Bike', 'Bike')], max_length=5)),
                ('SeatsAvailable', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=1)),
                ('Status', models.CharField(max_length=10)),
                ('HomeArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.volunteerarea')),
                ('RollNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.details')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HomeArea', models.CharField(max_length=50)),
                ('RollNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.details')),
            ],
        ),
        migrations.CreateModel(
            name='AvailableVolunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts', models.TimeField(auto_now_add=True)),
                ('PickupArea', models.CharField(choices=[('Arumbakkam', 'Arumbakkam'), ('', '')], max_length=50)),
                ('Volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.volunteer')),
            ],
        ),
    ]