from django.shortcuts import render , redirect
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from .forms import HeartDiseaseForm 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,"pages/main.html")

@login_required(login_url='acc_login')
def heart(request):
    
    if request.method == 'POST':
       
        form = HeartDiseaseForm(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    
    else:
        form = HeartDiseaseForm()

    return render(request, 'pages/heart.html', {'form': form})

@login_required(login_url='acc_login')
def heart_predictor(request):
    
    df = pd.read_csv("static/Heart_train.csv")
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1:]



    value = ''

    if request.method == 'POST':
        age = float(request.POST['age'])
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        fbs = float(request.POST['fbs'])
        restecg = float(request.POST['restecg'])
        thalach = float(request.POST['thalach'])
        exang = float(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = float(request.POST['slope'])
        ca = float(request.POST['ca'])
        thal = float(request.POST['thal'])

        user_data = np.array(
            (age,
             sex,
             cp,
             trestbps,
             chol,
             fbs,
             restecg,
             thalach,
             exang,
             oldpeak,
             slope,
             ca,
             thal)
        ).reshape(1, 13)

        #rf  = KNeighborsClassifier

        rf = RandomForestClassifier(
            n_estimators=16,
            criterion='entropy',
            max_depth=9
        )

        rf.fit(np.nan_to_num(X), Y)
        rf.score(np.nan_to_num(X), Y)
        predictions = rf.predict(user_data)

        if int(predictions[0]) == 1:
            value = 'have'
        elif int(predictions[0]) == 0:
            value = "don\'t have"

    return render(request,
                  'pages/heart.html',
                  {
                      'context': value,
                      'title': 'Heart Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'heart': True,
                      'form': HeartDiseaseForm(),
                  })
    

def register(request):
   # if request.method == 'POST':
   #if request.method == "POST":
   # 	form = NewUserForm(request.POST)
	#	if form.is_valid():
	#		user = form.save()
	#		login(request, user)
	#		messages.success(request, "Registration successful." )
	#		return redirect("main:homepage")
	#	    messages.error(request, "Unsuccessful registration. Invalid information.")
	#        form = NewUserForm()
	#return render (request=request, template_name="main/register.html", context={"register_form":form})
    return render(request,
            'pages/register.html',
            {
                'title' : ' registration form',
                'register':True,
                'active': 'btn btn-success peach-gradient text-white',
                'form': registerForm(),
    })