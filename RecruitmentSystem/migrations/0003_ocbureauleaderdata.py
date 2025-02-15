# Generated by Django 4.2.4 on 2024-05-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecruitmentSystem', '0002_ocdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='OCBureauLeaderData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocbureauleadername', models.CharField(max_length=100)),
                ('ocbureauleaderusername', models.CharField(max_length=50)),
                ('ocbureauleaderpassword', models.CharField(max_length=50)),
                ('ocbureauleaderid', models.CharField(max_length=20)),
                ('ocbureauleaderemail', models.EmailField(max_length=254)),
                ('ocbureauleadergender', models.CharField(max_length=10)),
                ('ocbureauleaderbureau', models.CharField(max_length=100)),
            ],
        ),
    ]
