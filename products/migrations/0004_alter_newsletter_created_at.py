# Generated by Django 4.0.3 on 2022-03-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_newsletter_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
    ]