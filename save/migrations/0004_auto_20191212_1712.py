# Generated by Django 2.2.7 on 2019-12-12 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('save', '0003_saved_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType'),
        ),
    ]