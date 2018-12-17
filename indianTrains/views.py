from django.shortcuts import render
import requests, json
from django.http import HttpResponse
# Create your views here.

# global part
api_key = "j3whwk24af"
base_url = "https://api.railwayapi.com/v2/live/train/"

def homepage(request):
    print("hello TheTrainApp")
    return render(request, 'index.html')

def liveStatus(request):
    return render(request, 'liveStatus.html')

def get_status(request):
    date = ""
    train_number = ""

    if(request.method == "POST"):
        train_number = request.POST['train_no']
        date = request.POST['date']

    arr = date.split("-")
    date = arr[2] + "-" + arr[1] + "-" + arr[0]
    print(train_number)
    print(date)
    complete_url = base_url + train_number + "/date/" + date + "/apikey/" + api_key + "/"
    print(complete_url)
    response = requests.get(complete_url)

    result = response.json()
    station_data = []
    print(result["response_code"])
    if(result["response_code"] == 200):
        # print(result)
        for list in result["route"]:
            str = list["station"]["name"] + " " + list["station"]["code"] + " " + list["schdep"] + " " + list["actdep"]
            # print(str)
            station_data.append(str)
        context = {
            "station_data": station_data,
            "current_station": result["position"],
            "response_code" : result["response_code"],
        }
        print(result["position"])
        for data in station_data:
            print(data)

    elif(result["response_code"] == 210):
        context= {
            "current_station" : "Train does not run on the specified date.",
            "response_code" : result["response_code"],
        }

    print(context["response_code"])
    return render(request, 'liveStatus.html', context)


def pnrStatus(request):
    return render(request, 'pnrStatus.html')

def pnr_status(request):
    pnr = ""
    context = {}
    if(request.method == "POST"):
        pnr = request.POST["pnr_number"]

    url = "https://api.railwayapi.com/v2/pnr-status/pnr/" + pnr + "/apikey/" + api_key + "/"

    response = requests.get(url)

    result = response.json()
    print(result)

    if(result["response_code"] == 200):
        passengers = []
        index = 0
        for passenger in result["passengers"]:
            temp = {
                "booking_status" : passenger["booking_status"],
                "current_status" : passenger["current_status"],
            }

            passengers.append(temp)
        print(passengers)
        context = {
            "response_code" : result["response_code"],
            "passengers" : passengers,
            "chart_prepared" : result["chart_prepared"],
        }

    elif(result["response_code"] == 221):
        context = {
            "response_code" : result["response_code"],
            "position" : "Invalid Pnr",
        }
    print(context)
    return render(request, 'pnrStatus.html', context)

def seatAvailability(request):
    return render(request, 'seatAvailability.html')

def seat_availability(request):
    train_number = "19051"
    source = ""
    dest = ""
    date = ""
    pref = ""
    quota = ""

    if(request.method == "POST"):
        train_number = request.POST["train_no"]
        source = request.POST["source"]
        dest = request.POST["dest"]
        date = request.POST["date"]
        pref = request.POST["pref"]
        quota = request.POST["quota"]

        arr = date.split("-")
        date = arr[2] + "-" + arr[1] + "-" + arr[0]
        print(date  )

    complete_url = "https://api.railwayapi.com/v2/check-seat/train/" + train_number + "/source/" + source + "/dest/" + dest + "/date/" + date + "/pref/" + pref + "/quota/" + quota + "/apikey/" + api_key + "/"

    response = requests.get(complete_url)
    print(response)
    # result = response.json()
    context = {}
    #
    # if(result["response_code"] == 200):
    #     context = {
    #         "response_code" : result["response_code"],
    #         "train_name" : result["train"]["name"],
    #         "train_number" : result["train"]["number"],
    #         "from" : result["from_station"]["name"],
    #         "to" : result["to_station"]["name"],
    #         "class" : pref,
    #         "quota" : quota,
    #         "availability" : result["availability"]
    #     }
    # elif(result["response_code"] == 210):
    #     context = {
    #         "response_code" : result["response_code"],
    #         "status" : "Train does not run on the specified date."
    #     }
    #
    # print(result)

    return render(request, 'seatAvailability.html', context)

def fare(request):
    return render(request, 'fare.html')

def train_fare(request):
    context = {}

    train_number = ""
    source = ""
    dest = ""
    age = ""
    class_code = ""
    quota = ""
    date = ""

    if(request.method == "POST"):
        train_number = request.POST["train_no"]
        source = request.POST["source"]
        dest = request.POST["destination"]
        age = request.POST["age"]
        class_code = request.POST["pref"]
        quota = request.POST["quota"]
        date = request.POST["date"]

        arr = date.split("-")
        date = arr[2] + "-" + arr[1] + "-" + arr[0]

    print(date)
    print(class_code)
    print(quota)
    url = "https://api.railwayapi.com/v2/fare/train/" + train_number + "/source/" + source + "/dest/" + dest + " /age/" + age + "/pref/" + class_code + "/quota/" + quota + "/date/" + date + "/apikey/"+ api_key + "/"

    response = requests.get(url)

    result = response.json()

    print(result)

    return render(request, 'fare.html')

def route(request):
    return render(request, 'route.html')

def get_route(request):
    context = {}
    train_number = ""
    if request.method == "POST":
        train_number = request.POST["train_no"]

    url = "https://api.railwayapi.com/v2/route/train/" + train_number + "/apikey/" + api_key + "/"
    response = requests.get(url)
    result = response.json()

    print(result["route"])
    if(result["response_code"] == 200):
        context = {
            "response_code" : result["response_code"],
            "train_name" : result["train"]["name"],
            "train_number" : train_number,
            "route" : result["route"],
        }
    return render(request, 'route.html', context)


def trains(request):
    return render(request, 'trainsBetweenStation.html')

def get_trains(request):
    context = {}
    source = ""
    dest = ""
    date = ""

    if(request.method == "POST"):
        source = request.POST["source"]
        dest = request.POST["destination"]
        date = request.POST["date"]

        arr = date.split("-")
        date = arr[2] + "-" + arr[1] + "-" + arr[0]

    url = "https://api.railwayapi.com/v2/between/source/" + source + "/dest/" + dest + "/date/" + date + "/apikey/" + api_key + "/"
    response = requests.get(url)
    result = response.json()

    for train in result["trains"]:
        print(train)

    if(result["response_code"] == 200):
        context = {
            "response_code" : result["response_code"],
            "trains" : result["trains"],
        }

    return render(request, 'trainsBetweenStation.html', context)
