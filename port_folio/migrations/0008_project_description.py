# Generated by Django 5.0.6 on 2025-03-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port_folio', '0007_alter_skill_displayed_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]
