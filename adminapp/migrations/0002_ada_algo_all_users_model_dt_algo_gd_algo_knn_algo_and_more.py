# Generated by Django 4.2.7 on 2023-11-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADA_ALGO',
            fields=[
                ('ADA_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'ADA_algo',
            },
        ),
        migrations.CreateModel(
            name='All_users_model',
            fields=[
                ('User_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_Profile', models.FileField(upload_to='images/')),
                ('User_Email', models.EmailField(max_length=50)),
                ('User_Status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'all_users',
            },
        ),
        migrations.CreateModel(
            name='DT_ALGO',
            fields=[
                ('DT_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'DT_algo',
            },
        ),
        migrations.CreateModel(
            name='GD_ALGO',
            fields=[
                ('GD_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'GD_algo',
            },
        ),
        migrations.CreateModel(
            name='KNN_ALGO',
            fields=[
                ('KNN_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'KNN_ALGO',
            },
        ),
        migrations.CreateModel(
            name='Logistic',
            fields=[
                ('Logistic_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'Logistic',
            },
        ),
        migrations.CreateModel(
            name='RandomForest',
            fields=[
                ('Random_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'RandomForest',
            },
        ),
        migrations.CreateModel(
            name='SVM_ALGO',
            fields=[
                ('SVM_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'SXM_algo',
            },
        ),
        migrations.CreateModel(
            name='XG_ALGO',
            fields=[
                ('XG_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'XG_algo',
            },
        ),
    ]
