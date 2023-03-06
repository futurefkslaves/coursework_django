# Generated by Django 4.1.7 on 2023-03-06 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peticions', '0005_alter_peticions_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='peticions',
            name='creator',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]