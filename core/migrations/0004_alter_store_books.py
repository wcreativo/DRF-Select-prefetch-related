# Generated by Django 4.0.4 on 2022-05-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_store_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='books',
            field=models.ManyToManyField(related_name='stores_contain_it', to='core.book'),
        ),
    ]