# Generated by Django 5.1.1 on 2024-10-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="experiment",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="experiment",
            name="description",
        ),
        migrations.RemoveField(
            model_name="experiment",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="experiment",
            name="file",
            field=models.FileField(null=True, upload_to="experiments/"),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="id",
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
