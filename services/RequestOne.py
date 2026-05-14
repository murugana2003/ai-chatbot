import os
import json


def writeFile():
    print("New File")
    with open("alerts.txt", "w") as f:
        f.write("Motion detected at Front Door\n")
        f.write("Motion detected at Back Front Door\n")
        f.write("Motion detected at Back Midlee Door\n adfafaf")

    print(os.path.abspath("alerts.txt"))


data = {
    "camera": "Front Door",
    "motion": True
}

def writeJson():
    with open("alerts.json", "w") as f:
        json.dump(data, f)

def readJson():
    with open("alerts.json", "r") as f:
        print(json.load(f))



def appendFile():
    with open("alerts.txt", "a") as f:
        f.write("Motion detected at Back Doora\n")


def readFile():
    with open("alerts.txt", "r") as f:
       print(f.read())
