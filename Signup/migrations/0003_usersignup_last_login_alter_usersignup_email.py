# Generated by Django 4.2.3 on 2024-01-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Signup", "0002_remove_usersignup_repassword"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersignup",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AlterField(
            model_name="usersignup",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]