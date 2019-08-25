from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random


def index(request):
    if 'gold' not in request.session:
        request.session["gold"] = 0
        request.session["activities"] = []
    return render(request, "ninja_gold_app/index.html")

def process_money(request):
    print("PROCESS")
    if request.method == "POST":
        print(request.POST["building"], "?????????")
        building = request.POST["building"]
        if building == "farm":
            gold_to_add = random.randint(10,20)
            request.session["gold"] += gold_to_add
        elif building == "cave":
            gold_to_add = random.randint(5,10)
            request.session["gold"] += gold_to_add
        elif building == "house":
            gold_to_add = random.randint(2,5)
            request.session["gold"] += gold_to_add
        else:
            gold_to_add = random.randint(-50,50)
            request.session["gold"] += gold_to_add
        
        request.session["activities"].insert(0, {
                "gold": gold_to_add,
                "building": building,
                "time": datetime.strftime(datetime.now(), "%m/%d/%Y, %H:%M:%S %p")
            })
        print(request.session["activities"][0])
    return redirect('/')