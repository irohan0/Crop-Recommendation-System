from django.shortcuts import render
from joblib import load

model=load('./savedModels/model.joblib')

# Create your views here.

def display_csv(request):
    with open('C:/Users/Rohan/OneDrive/Desktop/TRINIT_594092-U9EC5D62_ML3-/Crop_recommendation.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        column_index = header.index('label')
        column_values = [row[column_index] for row in reader]
    return render(request, 'result.html', {'column_values': column_values})


def pridictor(request):
    return render(request,'afilter.html')

def info(request):

    n=request.GET['nitro']
    p=request.GET['phos']
    k=request.GET['Potassium']
    temp=request.GET['temp']
    humid=request.GET['first']
    ph=request.GET['ph']
    rain=request.GET['rain']

    y_pred = [[n,p,k,temp,humid,ph,rain]]
    x= model.predict(y_pred)
    
    print(x)


    return render(request, 'result.html',{'result' :x})