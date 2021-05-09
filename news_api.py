
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
