# Generated by Django 4.1.6 on 2023-02-05 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='departments',
            field=models.ManyToManyField(blank=True, help_text='user will get all permissions granted to this department', related_name='users_in_department', to='accounts.department'),
        ),
    ]
