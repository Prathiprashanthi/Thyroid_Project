from django.shortcuts import render,redirect
from django.contrib import messages
import time
from mainapp.models import *
from userapp.models import *
from adminapp.models import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from django.core.files.storage import default_storage
import pytz
from datetime import datetime
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score,classification_report
# Create your views here.
def user_dashboard(request):
    prediction_count =  User_details.objects.all().count()
    print(prediction_count)
    user_id = request.session["User_id"]
    user =  User_details.objects.get(User_id = user_id)
    
    if user.Last_Login_Time is None:
        IST = pytz.timezone('Asia/Kolkata')
        current_time_ist = datetime.now(IST).time()
        user.Last_Login_Time = current_time_ist
        user.save()
    return render(request,'user/user_dashboard.html', {'predictions' : prediction_count, 'la' : user})

def user_profile(request):
    user_id = request.session["User_id"]
    user = User_details.objects.get(User_id = user_id)
    if request.method == 'POST':
        user_name = request.POST.get('userName')
        user_age = request.POST.get('userAge')
        user_phone = request.POST.get('userPhNum')
        user_email = request.POST.get('userEmail')
        user_address = request.POST.get("userAddress")
        
        # user_img = request.POST.get("userimg")

        user.Full_name = user_name
        user.Age = user_age
        user.Address = user_address
        user.Phone_Number = user_phone
        user.Email=user_email
       

        if len(request.FILES) != 0:
            image = request.FILES['profilepic']
            user.Image = image
            user.Full_name = user_name
            user.Age = user_age
            user.Address = user_address
            user.Phone_Number = user_phone
            user.Email=user_email
            user.Address=user_address
            
            user.save()
            messages.success(request, 'Updated SUccessfully...!')
        else:
            user.Full_name = user_name
            user.Age = user_age
            user.save()
            messages.success(request, 'Updated SUccessfully...!')
            
    context = {"i":user}
    return render(request,'user/user_profile.html',context)

def user_feedback(request):
    id=request.session["User_id"]
    uusser=User_details.objects.get(User_id=id)
    if request.method == "POST":
        rating=request.POST.get("rating")
        review=request.POST.get("review")
        # print(sentiment)        
        # print(rating)
        sid=SentimentIntensityAnalyzer()
        score=sid.polarity_scores(review)
        sentiment=None
        if score['compound']>0 and score['compound']<=0.5:
            sentiment='positive'
        elif score['compound']>=0.5:
            sentiment='very positive'
        elif score['compound']<-0.5:
            sentiment='negative'
        elif score['compound']<0 and score['compound']>=-0.5:
            sentiment=' very negative'
        else :
            sentiment='neutral'
        Feedback.objects.create(Rating=rating,Review=review,Sentiment=sentiment,Reviewer=uusser)
        messages.success(request,'Feedback recorded')
        return redirect('user_feedback')
    return render(request,'user/user_feedback.html')

def user_predict(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        T4U = request.POST.get('T4U')
        onthyroxine = request.POST.get('onthyroxine')
        T3 = request.POST.get('T3')
        FTI =request.POST.get('FTI')
        TT4= request.POST.get('TT4')
        TSH = request.POST.get('TSH')
        age = float(age)
        if sex == 0:
            gender = "male"
        else:
            gender = "female"
        context = {'gender': gender}
        
        T4U = float(T4U)
        T3 = float(T3)
        FTI = float(FTI)
        TT4=float(TT4)
        TSH=float(TSH )
            
       
        import pickle
        file_path = 'Thyroid_diesease/rfc_thyroid.pkl'  # Path to the saved model file

        with open(file_path, 'rb') as file:
            loaded_model = pickle.load(file)
            res =loaded_model.predict([[age,sex,T4U,onthyroxine,T3,FTI,TT4,TSH]])
            # res=loaded_model.predict([[25,1,50.125,12.0255,0.15,99.255,45.325]])

            dataset = Upload_dataset_model.objects.last()
            # print(dataset.Dataset)
            df=pd.read_csv(dataset.Dataset.path)
           
            x = df.drop('binaryClass', axis = 1)
            y = df['binaryClass']
            import imblearn
            from imblearn.over_sampling import SMOTE

            ros = SMOTE()  # You need to add parentheses to create an instance
            X_oversample, y_oversample = ros.fit_resample(x, y)

            print(X_oversample.shape)
            print(y_oversample.shape)

            from sklearn.model_selection import train_test_split

            X_train,X_test,y_train,y_test = train_test_split(X_oversample,y_oversample,random_state=1,test_size=0.2)
            from xgboost import XGBClassifier
           #  XGBoost

            XGB = XGBClassifier()
            XGB.fit(X_train, y_train)

            # prediction
            train_prediction= XGB.predict(X_train)
            test_prediction= XGB.predict(X_test)
            print('*'*20)

            # evaluation
            from sklearn.metrics import accuracy_score
            print('test accuracy:',accuracy_score(y_test,test_prediction))
            print('train accuracy:',accuracy_score(y_train,train_prediction))
            print('*'*20)

            # cross validation score
            from sklearn.model_selection import cross_val_score
            score=cross_val_score(XGB,x,y,cv=5)
            print(score.mean())
            print('*'*20)

            print(classification_report(y_test,test_prediction))

            print('*'*20)


            XGB_HSC = accuracy_score(y_test,test_prediction)
            print(f"{round(XGB_HSC*100,2)}% Accurate")
            from sklearn.metrics import accuracy_score,precision_score,recall_score
            accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
            precession = round(precision_score(test_prediction,y_test,average = 'macro')*100, 2)
            recall = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
            f1_score = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
            print(precession, accuracy,recall, f1_score,'uuuuuuuuuuuuuuuuuuuuuuuuuuu')
            x=0
            if res == 0:
                x = 0
                messages.success(request,"Thyroid Is Not Detected")
            else:
                x=1
                messages.warning(request,"Thyroid Is Detected")
            print(x)
            context = {'accc': accuracy,'pre': precession,'f1':f1_score,'call':recall,'res':x}
            print(type(res), 'ttttttttttttttttttttttttt')
            print(res)
            return render(request, 'user/user_result.html',context)
    return render(request,'user/user_predict.html')

def user_result(request):
    return render(request,'user/user_result.html')
def userlogout(req):
    user_id = req.session["User_id"]
    user = User_details.objects.get(User_id = user_id) 
    t = time.localtime()
    user.Last_Login_Time = t
    current_time = time.strftime('%H:%M:%S', t)
    user.Last_Login_Time = current_time
    current_date = time.strftime('%Y-%m-%d')
    user.Last_Login_Date = current_date
    user.save()
    messages.info(req, 'You are logged out..')
    # print(user.Last_Login_Time)
    # print(user.Last_Login_Date)
    return redirect('user_login')