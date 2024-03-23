# Generated by Django 4.2.3 on 2024-03-15 17:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("age5to12years", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="medicinedisease",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="medicinedisease",
            name="disease",
        ),
        migrations.RemoveField(
            model_name="medicinedisease",
            name="medicine",
        ),
        migrations.DeleteModel(
            name="Medicine",
        ),
        migrations.DeleteModel(
            name="MedicineDisease",
        ),
    ]