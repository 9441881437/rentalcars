# Generated by Django 5.0.2 on 2024-03-02 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_page', '0002_rename_b_loginmodels_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField(max_length=10)),
            ],
        ),
    ]
