# Generated by Django 5.1.6 on 2025-03-04 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port_folio', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=150)),
                ('degree', models.CharField(max_length=50)),
                ('years', models.CharField(max_length=15)),
                ('gpa', models.CharField(max_length=15)),
                ('current', models.CharField(choices=[('Completed', 'Completed'), ('Ongoing', 'Ongoing')], max_length=10)),
            ],
        ),
    ]
