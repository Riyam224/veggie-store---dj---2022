# Generated by Django 4.0.3 on 2022-03-25 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
                ('phone', models.CharField(max_length=50, verbose_name='phone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('website', models.CharField(max_length=50, verbose_name='website')),
                ('message', models.TextField(verbose_name='message')),
                ('subject', models.CharField(max_length=50, verbose_name='subject')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]