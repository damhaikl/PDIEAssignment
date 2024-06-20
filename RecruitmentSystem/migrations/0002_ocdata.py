# Generated by Django 4.2.4 on 2024-05-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecruitmentSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OCData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocname', models.CharField(max_length=100)),
                ('ocusername', models.CharField(max_length=50)),
                ('ocpassword', models.CharField(max_length=50)),
                ('ocid', models.CharField(max_length=20)),
                ('ocemail', models.EmailField(max_length=254)),
                ('ocgender', models.CharField(max_length=10)),
                ('ocbureau', models.CharField(max_length=100)),
            ],
        ),
    ]
