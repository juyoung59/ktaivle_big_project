# Generated by Django 4.2 on 2023-06-19 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chat",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]