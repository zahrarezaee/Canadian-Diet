from django.shortcuts import render
from .forms import ageForm
from .models import Serving
from .models import Groups
from .models import directional
from random import shuffle
from .models import Foods
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        genderr = request.POST['gender']
        age = request.POST['age']
        resault = []
        allServing = Serving.objects.filter(ages = age, gender = genderr)
        #return HttpResponse(len(allServing))
        for serve in allServing:
            fgidd = serve.fgid
            serveNum = serve.servings
            if serveNum == "7 to 8":
                foods = list(Foods.objects.filter(fgid=fgidd))
                shuffle(foods)
                helpFoods = foods[0:7]
                resault.append(helpFoods)
                shuffle(foods)
                helpFoods = foods[0:8]
                resault.append(helpFoods)
            elif serveNum == "8 to 10":
                foods = list(Foods.objects.filter(fgid=fgidd))
                shuffle(foods)
                helpFoods = foods[0:8]
                resault.append(helpFoods)
                shuffle(foods)
                helpFoods = foods[0:9]
                resault.append(helpFoods)
                shuffle(foods)
                helpFoods = foods[0:10]
                resault.append(helpFoods)
            elif serveNum == "6 to 7":
                foods = list(Foods.objects.filter(fgid=fgidd))
                shuffle(foods)
                helpFoods = foods[0:6]
                resault.append(helpFoods)
                shuffle(foods)
                helpFoods = foods[0:7]
                resault.append(helpFoods)
            elif serveNum == "3 to 4":
                foods = list(Foods.objects.filter(fgid=fgidd))
                shuffle(foods)
                helpFoods = foods[0:3]
                resault.append(helpFoods)
                shuffle(foods)
                helpFoods = foods[0:4]
                resault.append(helpFoods)
            elif serveNum == "1 to 2":
                foods = list(Foods.objects.filter(fgid=fgidd))
                shuffle(foods)
                helpFoods = foods[0:1]
                resault.append(helpFoods)
                shuffle(foods)
                helpFoods = foods[0:2]
                resault.append(helpFoods)
            else:

                intServe = int(serveNum)
                foods = list(Foods.objects.filter(fgid = fgidd))
                shuffle(foods)
                helpFoods = foods[0:intServe]
                resault.append(helpFoods)
        return render(request,'answer.html',{'foodList':resault})



    else:
        AgeForm = ageForm()
        return render(request, 'questions.html', {'form': AgeForm})