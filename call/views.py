from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import serial, json
from .models import call

# Create your views here.
@csrf_exempt
def home(request):
    #print(request.POST['data'])
    if request.POST['date']=='man':
        gender = 'man'
    elif request.POST['date']=='woman':
        gender = 'woman'
    else:
        gender = 'anybody'
    new_call = call(
        state = "대기중",
        gender_filter = gender
    )
    new_call.save()
    return render(request,'#')
