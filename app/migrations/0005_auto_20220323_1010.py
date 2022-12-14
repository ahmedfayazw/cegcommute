# Generated by Django 3.2.12 on 2022-03-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_volunteer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='availablevolunteer',
            name='Note',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='availablevolunteer',
            name='PickupArea',
            field=models.CharField(choices=[('Arumbakkam', 'Arumbakkam'), ('AnnaNagar', 'AnnaNagar'), ('Adyar', 'Adyar'), ('Alwarpet', 'Alwarpet'), ('Alappakkam', 'Alappakkam'), ('AlwarThiruNagar', 'AlwarThiruNagar'), ('Ayyanambakkam', 'Ayyanambakkam'), ('BesantNagar', 'BesantNagar'), ('CMBT', 'CMBT'), ('Chrompet', 'Chrompet'), ('Egmore', 'Egmore'), ('Guindy', 'Guindy'), ('Iyyapanthangal', 'Iyyapanthangal'), ('KKNagar', 'KKNagar'), ('Kattupakkam', 'Kattupakkam'), ('Kodambakkam', 'Kodambakkam'), ('Kundrathur', 'Kundrathur'), ('Meenambakkam', 'Meenambakkam'), ('Maduravayal', 'Maduravayal'), ('Mylapore', 'Mylapore'), ('Mogappair', 'Mogappair'), ('Nandanam', 'Nandanam'), ('Nungambakkam', 'Nungambakkam'), ('Nandambakkam', 'Nandambakkam'), ('Nasaratpet', 'Nasaratpet'), ('Porur', 'Porur'), ('Poonamallee', 'Poonamallee'), ('Purasaiwalkam', 'Purasaiwalkam'), ('Pudupet', 'Pudupet'), ('Royapuram', 'Royapuram'), ('Ramapuram', 'Ramapuram'), ('Saidapet', 'Saidapet'), ('TNagar', 'TNagar'), ('Teynampet', 'Teynampet'), ('Thiruvanmiyur', 'Thiruvanmiyur'), ('Virugambakkam', 'Virugambakkam'), ('Vadapalani', 'Vadapalani'), ('Velachery', 'Velachery'), ('Valasaravakkam', 'Valasaravakkam')], max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='Address',
            field=models.CharField(choices=[('Arumbakkam', 'Arumbakkam'), ('AnnaNagar', 'AnnaNagar'), ('Adyar', 'Adyar'), ('Alwarpet', 'Alwarpet'), ('Alappakkam', 'Alappakkam'), ('AlwarThiruNagar', 'AlwarThiruNagar'), ('Ayyanambakkam', 'Ayyanambakkam'), ('BesantNagar', 'BesantNagar'), ('CMBT', 'CMBT'), ('Chrompet', 'Chrompet'), ('Egmore', 'Egmore'), ('Guindy', 'Guindy'), ('Iyyapanthangal', 'Iyyapanthangal'), ('KKNagar', 'KKNagar'), ('Kattupakkam', 'Kattupakkam'), ('Kodambakkam', 'Kodambakkam'), ('Kundrathur', 'Kundrathur'), ('Meenambakkam', 'Meenambakkam'), ('Maduravayal', 'Maduravayal'), ('Mylapore', 'Mylapore'), ('Mogappair', 'Mogappair'), ('Nandanam', 'Nandanam'), ('Nungambakkam', 'Nungambakkam'), ('Nandambakkam', 'Nandambakkam'), ('Nasaratpet', 'Nasaratpet'), ('Porur', 'Porur'), ('Poonamallee', 'Poonamallee'), ('Purasaiwalkam', 'Purasaiwalkam'), ('Pudupet', 'Pudupet'), ('Royapuram', 'Royapuram'), ('Ramapuram', 'Ramapuram'), ('Saidapet', 'Saidapet'), ('TNagar', 'TNagar'), ('Teynampet', 'Teynampet'), ('Thiruvanmiyur', 'Thiruvanmiyur'), ('Virugambakkam', 'Virugambakkam'), ('Vadapalani', 'Vadapalani'), ('Velachery', 'Velachery'), ('Valasaravakkam', 'Valasaravakkam')], max_length=255),
        ),
        migrations.AlterField(
            model_name='studentarea',
            name='Area',
            field=models.CharField(choices=[('Arumbakkam', 'Arumbakkam'), ('AnnaNagar', 'AnnaNagar'), ('Adyar', 'Adyar'), ('Alwarpet', 'Alwarpet'), ('Alappakkam', 'Alappakkam'), ('AlwarThiruNagar', 'AlwarThiruNagar'), ('Ayyanambakkam', 'Ayyanambakkam'), ('BesantNagar', 'BesantNagar'), ('CMBT', 'CMBT'), ('Chrompet', 'Chrompet'), ('Egmore', 'Egmore'), ('Guindy', 'Guindy'), ('Iyyapanthangal', 'Iyyapanthangal'), ('KKNagar', 'KKNagar'), ('Kattupakkam', 'Kattupakkam'), ('Kodambakkam', 'Kodambakkam'), ('Kundrathur', 'Kundrathur'), ('Meenambakkam', 'Meenambakkam'), ('Maduravayal', 'Maduravayal'), ('Mylapore', 'Mylapore'), ('Mogappair', 'Mogappair'), ('Nandanam', 'Nandanam'), ('Nungambakkam', 'Nungambakkam'), ('Nandambakkam', 'Nandambakkam'), ('Nasaratpet', 'Nasaratpet'), ('Porur', 'Porur'), ('Poonamallee', 'Poonamallee'), ('Purasaiwalkam', 'Purasaiwalkam'), ('Pudupet', 'Pudupet'), ('Royapuram', 'Royapuram'), ('Ramapuram', 'Ramapuram'), ('Saidapet', 'Saidapet'), ('TNagar', 'TNagar'), ('Teynampet', 'Teynampet'), ('Thiruvanmiyur', 'Thiruvanmiyur'), ('Virugambakkam', 'Virugambakkam'), ('Vadapalani', 'Vadapalani'), ('Velachery', 'Velachery'), ('Valasaravakkam', 'Valasaravakkam')], max_length=50),
        ),
        migrations.AlterField(
            model_name='volunteerarea',
            name='Area',
            field=models.CharField(choices=[('Arumbakkam', 'Arumbakkam'), ('AnnaNagar', 'AnnaNagar'), ('Adyar', 'Adyar'), ('Alwarpet', 'Alwarpet'), ('Alappakkam', 'Alappakkam'), ('AlwarThiruNagar', 'AlwarThiruNagar'), ('Ayyanambakkam', 'Ayyanambakkam'), ('BesantNagar', 'BesantNagar'), ('CMBT', 'CMBT'), ('Chrompet', 'Chrompet'), ('Egmore', 'Egmore'), ('Guindy', 'Guindy'), ('Iyyapanthangal', 'Iyyapanthangal'), ('KKNagar', 'KKNagar'), ('Kattupakkam', 'Kattupakkam'), ('Kodambakkam', 'Kodambakkam'), ('Kundrathur', 'Kundrathur'), ('Meenambakkam', 'Meenambakkam'), ('Maduravayal', 'Maduravayal'), ('Mylapore', 'Mylapore'), ('Mogappair', 'Mogappair'), ('Nandanam', 'Nandanam'), ('Nungambakkam', 'Nungambakkam'), ('Nandambakkam', 'Nandambakkam'), ('Nasaratpet', 'Nasaratpet'), ('Porur', 'Porur'), ('Poonamallee', 'Poonamallee'), ('Purasaiwalkam', 'Purasaiwalkam'), ('Pudupet', 'Pudupet'), ('Royapuram', 'Royapuram'), ('Ramapuram', 'Ramapuram'), ('Saidapet', 'Saidapet'), ('TNagar', 'TNagar'), ('Teynampet', 'Teynampet'), ('Thiruvanmiyur', 'Thiruvanmiyur'), ('Virugambakkam', 'Virugambakkam'), ('Vadapalani', 'Vadapalani'), ('Velachery', 'Velachery'), ('Valasaravakkam', 'Valasaravakkam')], max_length=50),
        ),
    ]
