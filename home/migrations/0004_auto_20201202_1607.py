# Generated by Django 3.1.3 on 2020-12-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
