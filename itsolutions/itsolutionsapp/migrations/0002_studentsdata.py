# Generated by Django 4.1.4 on 2023-01-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsolutionsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('course', models.EmailField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
