#Akhbaar padhke sunaao:-

# problem statement:-

# The task you have to perform it to read the news using python.build a program that
# will give you daily top 10 latest news for that you have to check the website https
# ://newsapi.org/ which gives the news api first you have to create a account on that
# website, and then you will get free news api.

# after getting the news api use this function to read the news:-
# def(str):
#     from win32.client import Dispatch
#     speak=Dispatch("SAPI.Spvoice")
#     speak.speak(str)

# if __name__ == '__main__':
#        speak("you are the best my freind")
# ------------------------------------------------------------------------------------
import requests
import json

# below function speaks what we give to them.
def speak(str):
  from win32com.client import Dispatch
  speak = Dispatch("SAPI.spvoice")
  speak.Speak(str)

if __name__ == '__main__':
    speak("News for today lets begin!")

    url =  "https://newsapi.org/v2/everything?q=bitcoin&apiKey=8919f919db1843ffb625a36e79cec21d"

    request = requests.get(url).text #url ke text ko padhne ke liye convert kare.
    my_json = json.loads(request) #json ki madad se url ko readable banaye.
    arts = my_json["articles"] #jo read karna hai wo btaye for ex articles.

    for article in arts:
        speak(article["title"])#title read karna hai bas.
        speak("moving on to the next news..listen carefully")