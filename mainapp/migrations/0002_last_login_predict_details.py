# Generated by Django 4.2.7 on 2023-11-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Last_login',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Login_Time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'last_login',
            },
        ),
        migrations.CreateModel(
            name='Predict_details',
            fields=[
                ('predict_id', models.AutoField(primary_key=True, serialize=False)),
                ('Field_1', models.CharField(max_length=60, null=True)),
                ('Field_2', models.CharField(max_length=60, null=True)),
                ('Field_3', models.CharField(max_length=60, null=True)),
                ('Field_4', models.CharField(max_length=60, null=True)),
                ('Field_5', models.CharField(max_length=60, null=True)),
                ('Field_6', models.CharField(max_length=60, null=True)),
                ('Field_7', models.CharField(max_length=60, null=True)),
                ('Field_8', models.CharField(max_length=60, null=True)),
            ],
            options={
                'db_table': 'predict_detail',
            },
        ),
    ]
