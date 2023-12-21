from django.shortcuts import render,redirect
from django.contrib import messages
from userapp.models import*
from adminapp.models import *
from django.contrib import messages
from django.core.paginator import Paginator
from mainapp.models import User_details
from adminapp.models import  Upload_dataset_model
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from imblearn.over_sampling import SMOTE
import pandas as pd
from sklearn.metrics import accuracy_score,classification_report
# Create your views here.
def admin_dashboard(request):
    all_users_count =  User_details.objects.all().count()
    pending_users_count = User_details.objects.filter(User_Status = 'Pending').count()
    rejected_users_count = User_details.objects.filter(User_Status = 'removed').count()
    accepted_users_count = User_details.objects.filter(User_Status = 'accepted').count()
    return render(request,'admin/admin_dashboard.html',{'a' : all_users_count, 'b' : pending_users_count, 'c' : rejected_users_count, 'd' : accepted_users_count})

def admin_pendings(request):
    pending = User_details.objects.filter(User_Status = 'Pending')
    paginator = Paginator(pending, 5) 
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'admin/admin_pendinguser.html', { 'user' : post})

def admin_allusers(request):
    all_users = User_details.objects.all()
    paginator = Paginator(all_users, 5)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'admin/admin_allusers.html', {"allu" : all_users, 'user' : post})
#Deleet user button in allusers
def delete_user(request, id):
    User_details.objects.get(User_id = id).delete()
    messages.warning(request, 'User was Deleted..!')
    return redirect('admin_allusers')

# Acept users button
def accept_user(request, id):
    status_update = User_details.objects.get(User_id = id)
    status_update.User_Status = 'accepted'
    status_update.save()
    messages.success(request, 'User was accepted..!')
    return redirect('admin_pendings')

# Remove user button
def reject_user(request, id):
    status_update2 = User_details.objects.get(User_id = id)
    status_update2.User_Status = 'removed'
    status_update2.save()
    messages.warning(request, 'User was Rejected..!')
    return redirect('admin_pendings')
# def change_status(req, id):
#     status_update = User_details.objects.get(User_id = id)
#     if (status_update.User_Status == 'accepted'):
#         status_update.User_Status = 'rejected'
#     else:
#         status_update.User_Status = 'accepted'

#     status_update.save()
#     return redirect('allusers')



# Admin delete dataset button
def delete_dataset(request, id):
    dataset = Upload_dataset_model.objects.get(User_id = id).delete()
    messages.warning(request, 'Dataset was deleted..!')
    return redirect('admin_view')

def admin_upload(request):
    if request.method == 'POST':
        file = request.FILES['data_file']
        # print(file)
        file_size = str((file.size)/1024) +' kb'
        # print(file_size)
        Upload_dataset_model.objects.create(File_size = file_size, Dataset = file)
    return render(request,'admin/admin_upload.html')

def admin_view(request):
    dataset = Upload_dataset_model.objects.all()
    paginator = Paginator(dataset, 5)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    return render(request,'admin/admin_datasetviews.html', {'data' : dataset, 'user' : post})

def view_view(request):
    # df=pd.read_csv('heart.csv')
    data = Upload_dataset_model.objects.last()
    print(data,type(data),'sssss')
    file = str(data.Dataset)
    df = pd.read_csv(f'./media/{file}')
    table = df.to_html(table_id='data_table')
    return render(request,'admin/view.html', {'t':table})

def admin_Xg_algo(request):
    return render(request,'admin/admin_Xgboost.html') 

def XGBOOST_btn(request):
    dataset = Upload_dataset_model.objects.last()
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
    # evaluation
    from sklearn.metrics import accuracy_score,precision_score,recall_score,recall_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(test_prediction,y_test,average = 'macro')*100, 2)
    recall = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    f1_score = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    name = "XG Boost Algorithm"
    XG_ALGO.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1_score,Recall=recall,Name=name)
    data =XG_ALGO.objects.last()
    messages.success(request, 'Algorithm executed Successfully')
    return render(request,'admin/admin_Xgboost.html',{'i': data})

def admin_ada_algo(request):
    
    return render(request,'admin/admin_Adaboost.html')

def ADABoost_btn(request):
    dataset = Upload_dataset_model.objects.last()
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
    ada = AdaBoostClassifier()
    ada.fit(X_train, y_train)

    # prediction
    train_prediction= ada.predict(X_train)
    test_prediction= ada.predict(X_test)
    print('*'*20)

    # evaluation
    from sklearn.metrics import accuracy_score
    print('test accuracy:',accuracy_score(y_test,test_prediction))
    print('train accuracy:',accuracy_score(y_train,train_prediction))
    print('*'*20)

    # cross validation score
    from sklearn.model_selection import cross_val_score
    score=cross_val_score(ada,x,y,cv=5)
    print(score.mean())
    print('*'*20)

    print(classification_report(y_test,test_prediction))

    print('*'*20)
    ada_hsc = accuracy_score(y_test,test_prediction)
    print(f"{round(ada_hsc*100,2)}% Accurate")
    # evaluation
    from sklearn.metrics import accuracy_score,precision_score,recall_score,recall_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(test_prediction,y_test,average = 'macro')*100, 2)
    recall = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    f1_score = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    name = "ADA Boost Algorithm"
    ADA_ALGO.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1_score,Recall=recall,Name=name)
    data =ADA_ALGO.objects.last()
    messages.success(request, 'Algorithm executed Successfully')
    return render(request,'admin/admin_Adaboost.html',{'i': data})

def admin_Logistic_algo(request):
    return render(request,'admin/admin_Logistic.html')

def logistic_btn(request):
    dataset = Upload_dataset_model.objects.last()
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
    # logistic regression

    LR = LogisticRegression()
    LR.fit(X_train, y_train)


    # prediction
    train_prediction= LR.predict(X_train)
    test_prediction= LR.predict(X_test)
    print('*'*20)

    # evaluation
    from sklearn.metrics import accuracy_score
    print('test accuracy:',accuracy_score(y_test,test_prediction))
    print('train accuracy:',accuracy_score(y_train,train_prediction))
    print('*'*20)

    # cross validation score
    from sklearn.model_selection import cross_val_score
    score=cross_val_score(LR,x,y,cv=5)
    print(score.mean())
    print('*'*20)

    print(classification_report(y_test,test_prediction))

    print('*'*20)


    lr_HSC = accuracy_score(y_test,test_prediction)
    print(f"{round(lr_HSC*100,2)}% Accurate")
    # evaluation
    from sklearn.metrics import accuracy_score,precision_score,recall_score,recall_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(test_prediction,y_test,average = 'macro')*100, 2)
    recall = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    f1_score = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    name = "Logistic Algorithm"
    Logistic.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1_score,Recall=recall,Name=name)
    data =Logistic.objects.last()
    messages.success(request, 'Algorithm executed Successfully')
    return render(request,'admin/admin_Logistic.html',{'i': data})

def admin_knn_algo(request):
    return render(request,'admin/admin_knn.html') 

def KNN_btn(request):
    dataset = Upload_dataset_model.objects.last()
    df=pd.read_csv(dataset.Dataset.path)


    x = df.drop('binaryClass', axis = 1)
    y = df['binaryClass']
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

    import imblearn
    from imblearn.over_sampling import SMOTE

    ros = SMOTE()  # You need to add parentheses to create an instance
    X_oversample, y_oversample = ros.fit_resample(x, y)

    # print(X_oversample.shape)
    # print(y_oversample.shape)

    from sklearn.model_selection import train_test_split

    Xx_train,Xx_test,yy_train,yy_test = train_test_split(X_oversample,y_oversample,random_state=1,test_size=0.2)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    Xx_train=scaler.fit_transform(Xx_train)
    Xx_test= scaler.transform(Xx_test)

    # model
    knn_model=KNeighborsClassifier()
    knn_model.fit(Xx_train,yy_train)

    # prediction
    train_prediction= knn_model.predict(Xx_train)
    test_prediction= knn_model.predict(Xx_test)

    # evaluation
    print('*'*20)
    from sklearn.metrics import accuracy_score
    print('Test accuracy:',accuracy_score(yy_test,test_prediction))
    print('Train accuracy:',accuracy_score(yy_train,train_prediction))

    print('*'*20)
    result = confusion_matrix(yy_test, test_prediction)
    print("Confusion Matrix:")
    print(result)


    print('*'*20)
    #  prediction Summary by species
    print(classification_report(yy_test, test_prediction))


    print('*'*20)
    # Accuracy score
    Knn_SC = accuracy_score(test_prediction,yy_test)
    print(f"{round(Knn_SC*100,2)}% Accurate")


    # evaluation
    from sklearn.metrics import accuracy_score,precision_score,recall_score,recall_score
    accuracy = round(accuracy_score(yy_test,test_prediction)*100, 2)
    precession = round(precision_score(test_prediction,yy_test,average = 'macro')*100, 2)
    recall = round(recall_score(test_prediction,yy_test,average = 'macro')*100, 2)
    f1_score = round(recall_score(test_prediction,yy_test,average = 'macro')*100, 2)
    name = "KNN Algorithm"
    KNN_ALGO.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1_score,Recall=recall,Name=name)
    data =KNN_ALGO.objects.last()
    messages.success(request, 'Algorithm executed Successfully')
    return render(request,'admin/admin_knn.html',{'i': data})

def admin_Randomforest_algo(request):
    return render(request,'admin/admin_RandomForest.html')

def randomforest_btn(request):
    dataset = Upload_dataset_model.objects.last()
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
    rfc=RandomForestClassifier(random_state=42)
    rfc.fit(X_train,y_train)
    print('*'*20)

    # prediction
    train_prediction= rfc.predict(X_train)
    test_prediction= rfc.predict(X_test)
    print('*'*20)

    # evaluation
    from sklearn.metrics import accuracy_score
    print('test accuracy:',accuracy_score(y_test,test_prediction))
    print('train accuracy:',accuracy_score(y_train,train_prediction))
    print('*'*20)

    # cross validation score
    from sklearn.model_selection import cross_val_score
    score=cross_val_score(rfc,x,y,cv=5)
    print(score.mean())
    print('*'*20)

    #  prediction Summary by species
    # print(classification_report(y_test, test_prediction))
    print('*'*20)

    # Accuracy score
    RF_SC = accuracy_score(test_prediction,y_test)
    print(f"{round(RF_SC*100,2)}% Accurate")
    # evaluation
    from sklearn.metrics import accuracy_score,precision_score,recall_score,recall_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(test_prediction,y_test,average = 'macro')*100, 2)
    recall = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    f1_score = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    name = "Random Forest Algorithm"
    RandomForest.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1_score,Recall=recall,Name=name)
    data =RandomForest.objects.last()
    messages.success(request, 'Algorithm executed Successfully')
    
    return render(request,'admin/admin_RandomForest.html',{'i': data})

def admin_greadient_algo(request):
    return render(request,'admin/admin_greadient.html')

def GR_btn(request):
    dataset = Upload_dataset_model.objects.last()
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
    Gr =  GradientBoostingClassifier()
    Gr.fit(X_train, y_train)

    # prediction
    train_prediction= Gr.predict(X_train)
    test_prediction= Gr.predict(X_test)
    print('*'*20)

    # evaluation
    from sklearn.metrics import accuracy_score
    print('test accuracy:',accuracy_score(y_test,test_prediction))
    print('train accuracy:',accuracy_score(y_train,train_prediction))
    print('*'*20)

    # cross validation score
    from sklearn.model_selection import cross_val_score
    score=cross_val_score(Gr,x,y,cv=5)
    print(score.mean())
    print('*'*20)

    print(classification_report(y_test,test_prediction))

    print('*'*20)


    Gr_HSC = accuracy_score(y_test,test_prediction)
    print(f"{round(Gr_HSC*100,2)}% Accurate")
    # evaluation
    from sklearn.metrics import accuracy_score,precision_score,recall_score,recall_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(test_prediction,y_test,average = 'macro')*100, 2)
    recall = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    f1_score = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    name = "Gr Boost Algorithm"
    GD_ALGO.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1_score,Recall=recall,Name=name)
    data =GD_ALGO.objects.last()
    messages.success(request, 'Algorithm executed Successfully')
    return render(request,'admin/admin_greadient.html',{'i': data})

def admin_svm_algo(request):
    return render(request,'admin/admin_svm.html') 

def SVM_btn(request):
    dataset = Upload_dataset_model.objects.last()
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
    # support vector 

    svc=SVC()
    svc = AdaBoostClassifier()
    svc.fit(X_train, y_train)

    # prediction
    train_prediction= svc.predict(X_train)
    test_prediction= svc.predict(X_test)
    print('*'*20)

    # evaluation
    from sklearn.metrics import accuracy_score
    print('test accuracy:',accuracy_score(y_test,test_prediction))
    print('train accuracy:',accuracy_score(y_train,train_prediction))
    print('*'*20)

    # cross validation score
    from sklearn.model_selection import cross_val_score
    score=cross_val_score(svc,x,y,cv=5)
    print(score.mean())
    print('*'*20)

    print(classification_report(y_test,test_prediction))

    print('*'*20)


    svc_hsc = accuracy_score(y_test,test_prediction)
    print(f"{round(svc_hsc*100,2)}% Accurate")
    # evaluation
    from sklearn.metrics import accuracy_score,precision_score,recall_score,recall_score
    accuracy = round(accuracy_score(y_test,test_prediction)*100, 2)
    precession = round(precision_score(test_prediction,y_test,average = 'macro')*100, 2)
    recall = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    f1_score = round(recall_score(test_prediction,y_test,average = 'macro')*100, 2)
    name = "SVM Algorithm"
    SVM_ALGO.objects.create(Accuracy=accuracy,Precession=precession,F1_Score=f1_score,Recall=recall,Name=name)
    data =SVM_ALGO.objects.last()
    messages.success(request, 'Algorithm executed Successfully')
    return render(request,'admin/admin_svm.html',{'i': data})

def admin_dt_algo(request):
    return render(request,'admin/admin_DT.html') 

def Decisiontree_btn(request):
     # Load dataset
    dataset = Upload_dataset_model.objects.last()
    df = pd.read_csv(dataset.Dataset.path)

    # Data preprocessing with SMOTE
    x = df.drop('binaryClass', axis=1)
    y = df['binaryClass']
    ros = SMOTE()
    X_oversample, y_oversample = ros.fit_resample(x, y)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X_oversample, y_oversample, random_state=1, test_size=0.2)

    # Decision Tree
    DT = DecisionTreeClassifier()
    DT.fit(X_train, y_train)

    # Prediction
    train_pred = DT.predict(X_train)
    test_pred = DT.predict(X_test)

    # Accuracy
    print('Train accuracy:', accuracy_score(y_train, train_pred))
    print('Test accuracy:', accuracy_score(y_test, test_pred))

    # Cross-validation
    score = cross_val_score(DT, x, y, cv=5)
    print(score)
    print(score.mean())

    # Prediction Summary by species
    print(classification_report(y_test, test_pred))

    # Accuracy score
    DT_SC = accuracy_score(test_pred, y_test)
    print(f"{round(DT_SC*100, 2)}% Accurate")

    # Evaluation
    accuracy = round(accuracy_score(y_test, test_pred) * 100, 2)
    precession = round(precision_score(test_pred, y_test, average='macro') * 100, 2)
    recall = round(recall_score(test_pred, y_test, average='macro') * 100, 2)
    f1 = round(f1_score(test_pred, y_test, average='macro') * 100, 2)
    name = "Decision Tree Algorithm"

    # Save results to database
    DT_ALGO.objects.create(Accuracy=accuracy, Precession=precession, F1_Score=f1, Recall=recall, Name=name)
    data = DT_ALGO.objects.last()
    
    messages.success(request, 'Algorithm executed Successfully')
    return render(request, 'admin/admin_DT.html', {'i': data})

def admin_graph(request):
    details = XG_ALGO.objects.last()
    a = details.Accuracy
    deatails1 = ADA_ALGO.objects.last()
    b = deatails1.Accuracy
    details2 = KNN_ALGO.objects.last()
    c = details2.Accuracy
    deatails3 = SVM_ALGO.objects.last()
    d = deatails3.Accuracy
    details4 = DT_ALGO.objects.last()
    e = details4.Accuracy
    details5 = GD_ALGO.objects.last()
    f = details5.Accuracy
    details6 = Logistic.objects.last()
    g = details6.Accuracy
    details7 = RandomForest.objects.last()
    h = details7.Accuracy
    return render(request,'admin/admin_graph.html', {'xg':a,'ada':b,'knn':c,'sxm':d,'dt':e,'gr':f,'log':g, 'ran':h})

def admin_feedback(request):
    feed =Feedback.objects.all()
    return render(request,'admin/user_feedbacks.html', {'back':feed}) 

def admin_sentiment(request):
    fee = Feedback.objects.all()
    return render(request,'admin/user_setiment.html', {'cat':fee}) 

def admin_feedbackgraph(request):
    positive = Feedback.objects.filter(Sentiment = 'positive').count()
    very_positive = Feedback.objects.filter(Sentiment = 'very positive').count()
    negative = Feedback.objects.filter(Sentiment = 'negative').count()
    very_negative = Feedback.objects.filter(Sentiment = 'very negative').count()
    neutral = Feedback.objects.filter(Sentiment = 'neutral').count()
    context ={
        'vp': very_positive, 'p':positive, 'n':negative, 'vn':very_negative, 'ne':neutral
    }
    return render(request,'admin/user_feedback_graph.html',context) 
def admin_logout(req):
    messages.info(req, 'You are logged out..!')
    return redirect('admin_login')