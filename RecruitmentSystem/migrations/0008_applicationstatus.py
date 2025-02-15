# Generated by Django 4.2.4 on 2024-06-16 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RecruitmentSystem', '0007_selectedoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('student_application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='RecruitmentSystem.studentapplication')),
            ],
        ),
    ]
