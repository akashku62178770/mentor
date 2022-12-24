# Generated by Django 4.1.2 on 2022-10-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_alter_mentor_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentprofile",
            name="ambition",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="health",
            field=models.CharField(help_text="Any health issue!", max_length=50),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="hobby",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="interest",
            field=models.CharField(max_length=50),
        ),
    ]
