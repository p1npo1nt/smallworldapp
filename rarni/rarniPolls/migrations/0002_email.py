# Generated by Django 4.1.4 on 2022-12-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rarniPolls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
