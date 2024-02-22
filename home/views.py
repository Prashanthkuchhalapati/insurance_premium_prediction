from django.shortcuts import render,HttpResponse
import joblib

# Create your views here.
model = joblib.load('static/random_forest_regressor')

def index(request):
    #return HttpResponse("this is homepage")
    return render(request,'index.html')


def about(request):
    #return HttpResponse("this is about homepage")
    return render(request,'about.html')

def contact(request):
    #return HttpResponse("this is contact homepage")
    return render(request,'contact.html')

def prediction(request):

    #return HttpResponse("this is prediction homepage")
    if request.method == "post":
        print("enter into post request")
        age= int(request.POST.get('age'))
        sex= int(request.POST.get('sex'))
        bmi= int(request.POST.get('bmi'))
        children= int(request.POST.get('children'))
        smoker = request.POST.get('smoker')
        region = request.POST.get('region')

        print(age,sex,bmi,children,smoker,region)

        pred= models.Predict([[age,sex,bmi,children,smoker]])

        print(pred)

        output= {
            "output":pred
        }

        return render(request,'prediction.html',output)

    else:
        return render(request,'prediction.html')

