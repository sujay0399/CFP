# Generated by Django 2.2 on 2019-05-28 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_auto_20190528_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Conference'),
        ),
    ]