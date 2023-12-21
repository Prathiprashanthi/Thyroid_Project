from django.db import models

# Create your models here.
class Upload_dataset_model(models.Model):
    User_id = models.AutoField(primary_key = True)
    Dataset = models.FileField(null=True)
    File_size = models.CharField(max_length = 100) 
    Date_Time = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'upload_dataset'


class DATASET(models.Model):
    DS_ID = models.AutoField(primary_key = True)
    Age = models.IntegerField()
    Glucose = models.IntegerField() 
    BloodPressure = models.IntegerField()
    SkinThickness = models.IntegerField()
    Insulin = models.IntegerField()
    BMI = models.IntegerField()
    DiabetesPedigreeFunction = models.IntegerField() 
    Pregnancies = models.IntegerField()

    
    class Meta:
        db_table = 'Dataset'
        
class All_users_model(models.Model):
    User_id = models.AutoField(primary_key = True)
    user_Profile = models.FileField(upload_to = 'images/')
    User_Email = models.EmailField(max_length = 50)
    User_Status = models.CharField(max_length = 10)
    
    class Meta:
        db_table = 'all_users'
        
# ANM Algorithm
class ADA_ALGO(models.Model):
    ADA_ID = models.AutoField(primary_key = True)
    Accuracy = models.TextField(max_length = 100)
    Precession = models.TextField(max_length = 100) 
    F1_Score = models.TextField(max_length = 100)
    Recall = models.TextField(max_length = 100)
    Name = models.TextField(max_length = 100)
    
    class Meta:
        db_table = 'ADA_algo'
        
# Logistic Regression
class KNN_ALGO(models.Model):
    KNN_ID = models.AutoField(primary_key = True)
    Accuracy = models.TextField(max_length = 100)
    Precession = models.TextField(max_length = 100) 
    F1_Score = models.TextField(max_length = 100)
    Recall = models.TextField(max_length = 100)
    Name = models.TextField(max_length = 100)
    
    class Meta:
        db_table = 'KNN_ALGO'

class Logistic(models.Model):
    Logistic_ID = models.AutoField(primary_key = True)
    Accuracy = models.TextField(max_length = 100)
    Precession = models.TextField(max_length = 100) 
    F1_Score = models.TextField(max_length = 100)
    Recall = models.TextField(max_length = 100)
    Name = models.TextField(max_length = 100)
    
    class Meta:
        db_table = 'Logistic'
        
class RandomForest(models.Model):
    Random_ID = models.AutoField(primary_key = True)
    Accuracy = models.TextField(max_length = 100)
    Precession = models.TextField(max_length = 100) 
    F1_Score = models.TextField(max_length = 100)
    Recall = models.TextField(max_length = 100)
    Name = models.TextField(max_length = 100)
    
    class Meta:
        db_table = 'RandomForest'


# XG-Boost Algo
class XG_ALGO(models.Model):
    XG_ID = models.AutoField(primary_key = True)
    Accuracy = models.TextField(max_length = 100)
    Precession = models.TextField(max_length = 100) 
    F1_Score = models.TextField(max_length = 100)
    Recall = models.TextField(max_length = 100)
    Name = models.TextField(max_length = 100)
    
    class Meta:
        db_table = 'XG_algo'

# ADA Boost Algo
class GD_ALGO(models.Model):
    GD_ID = models.AutoField(primary_key = True)
    Accuracy = models.TextField(max_length = 100)
    Precession = models.TextField(max_length = 100) 
    F1_Score = models.TextField(max_length = 100)
    Recall = models.TextField(max_length = 100)
    Name = models.TextField(max_length = 100)
    
    class Meta:
        db_table = 'GD_algo'

# KNN Algo


# SXM Algo
class SVM_ALGO(models.Model):
    SVM_ID = models.AutoField(primary_key = True)
    Accuracy = models.TextField(max_length = 100)
    Precession = models.TextField(max_length = 100) 
    F1_Score = models.TextField(max_length = 100)
    Recall = models.TextField(max_length = 100)
    Name = models.TextField(max_length = 100)
    
    class Meta:
        db_table = 'SXM_algo'

# DECISION TREE Algo
class DT_ALGO(models.Model):
    DT_ID = models.AutoField(primary_key = True)
    Accuracy = models.TextField(max_length = 100)
    Precession = models.TextField(max_length = 100) 
    F1_Score = models.TextField(max_length = 100)
    Recall = models.TextField(max_length = 100)
    Name = models.TextField(max_length = 100)
    
    class Meta:
        db_table = 'DT_algo'
