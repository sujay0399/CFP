# Generated by Django 2.2 on 2019-06-03 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0011_auto_20190528_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Speaker'),
        ),
    ]
