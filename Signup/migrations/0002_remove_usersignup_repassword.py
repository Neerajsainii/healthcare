# Generated by Django 4.2.3 on 2024-01-29 04:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Signup", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usersignup",
            name="repassword",
        ),
    ]