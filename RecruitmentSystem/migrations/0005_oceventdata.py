# Generated by Django 4.2.4 on 2024-05-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecruitmentSystem', '0004_ocpresidentdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='OCEventData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oceventname', models.CharField(max_length=200)),
                ('oceventdate', models.DateField()),
                ('oceventtime', models.TimeField()),
                ('oceventlocation', models.CharField(max_length=200)),
                ('oceventdescription', models.TextField()),
                ('oceventocneeded', models.IntegerField()),
            ],
        ),
    ]
