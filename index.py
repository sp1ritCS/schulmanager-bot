timetable = {
    "montag": {
        "08:00": "Englisch",
        "08:45": "Geschichte",
        "09:30": "Deutsch",
        "10:15": "Pause",
        "10:35": "Französisch",
        "11:20": "Relligion",
        "12:05": "Aus",
        "23:59": "Aus",
    },
    "dienstag": {
        "08:00": "Geschichte",
        "08:45": "Englisch",
        "09:30": "Wirtschafts Informatik/SoG",
        "10:15": "Pause",
        "10:35": "Relligion",
        "11:20": "Mathematik",
        "12:05": "Deutsch",
        "23:59": "Aus",
    },
    "mittwoch": {
        "08:00": "Physik",
        "08:45": "Mathematik",
        "09:30": "Geographie",
        "10:15": "Pause",
        "10:35": "Wirtschaft und Recht/Sozialstunde",
        "11:20": "Französisch",
        "12:05": "Aus",
        "23:59": "Aus",
    },
    "donnerstag": {
        "08:00": "Physik",
        "08:45": "Französisch",
        "09:30": "Deutsch",
        "10:15": "Pause",
        "10:35": "Biologie",
        "11:20": "Musik",
        "12:05": "Mathematik",
        "23:59": "Aus",
    },
    "freitag": {
        "08:00": "Französisch",
        "08:45": "Geographie",
        "09:30": "Deutsch",
        "10:15": "Pause",
        "10:35": "Mathematik",
        "11:20": "Wirtschaft und Recht",
        "12:05": "Englisch",
        "23:59": "Aus",
    },
}

import selenium.webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import requests
import json
from googletrans import Translator
translator = Translator()
from datetime import datetime
from random import randint

driver = selenium.webdriver.Safari()
driver.get("https://login.schulmanager-online.de/#/modules/messenger/messages")

def login():
    username = driver.find_element_by_class_name("email-or-username-input")
    username.send_keys("marc-aurel-w@online.de")
    password = driver.find_element_by_id("password")
    password.send_keys("sycra2-rywmeh-hisziN")
    password.send_keys(Keys.RETURN)

def enterChat():
    print('Enter a channel id:')
    id = input()
    driver.get("https://login.schulmanager-online.de/#/modules/messenger/messages/" + id)

def send(text):
    textarea = driver.find_element_by_tag_name('textarea')
    textarea.send_keys(text)
    sendBtn = driver.find_element_by_class_name("send-button")
    sendBtn.send_keys(Keys.RETURN)
    oldMessage = text

def read():
    global message
    message = driver.find_elements_by_class_name("message-text")[-1].get_attribute('innerHTML')

def calc(arg):
    solution = str(eval(arg))
    solutionMessage = "Dein Ergebnis für die Aufgabe " + arg + " ist " + solution
    send(solutionMessage)

def corona():
    global response

    response = requests.post("Enter your WrapAPI Link", json={
      "wrapAPIKey": "EnterYourAPIToken"
    })
    response = response.json()
    response = response["data"]
    response = response["output"]

def trans(arg):
    print(arg)
    if(arg.startswith("de")):
        arg = arg.replace("de ", "")
        send("Original: " + arg + "\nDeutsch: " + str(translator.translate(arg, dest='de').text))
    elif(arg.startswith("en")):
        arg = arg.replace("en ", "")
        send("Original: " + arg + "\nEnglisch: " + str(translator.translate(arg, dest='en').text))
    elif(arg.startswith("fr")):
        arg = arg.replace("fr ", "")
        send("Original: " + arg + "\nFranzösisch: " + str(translator.translate(arg, dest='en').text))
    else:
        send("Diese Sprache kann ich noch nicht.")

def gong():
    now = datetime.now()
    dayNum = datetime.today().weekday()
    if(dayNum == 5 or dayNum == 6):
        return
    current_time = now.strftime("%H:%M:%S")
    if(current_time == "8:00:00"):
        send("Gong")
    elif(current_time == "8:45:00"):
        send("Gong")
    elif(current_time == "9:30:00"):
        send("Gong")
    elif(current_time == "10:15:00"):
        send("Gong")
    elif(current_time == "10:35:00"):
        send("Gong")
    elif(current_time == "11:20:00"):
        send("Gong")
    elif(current_time == "12:05:00"):
        send("Gong")
    elif(current_time == "12:50:00"):
        send("Gong")

def ssp(arg):
    random = randint(1, 3)
    # 1: Schere, 2: Stein, 3: Papier
    if(arg.upper() == "SCHERE" or arg.upper() == "STEIN" or arg.upper() == "PAPIER"):
        if(random == 1):
            if(arg.upper() == "SCHERE"):
                send("Unentschieden! Ich hatten auch Schere.")
            elif(arg.upper() == "STEIN"):
                send("Du hast gewonnen! Ich hatte Schere.")
            elif(arg.upper() == "PAPIER"):
                send("Du hast verloren! Ich hatte Schere.")
        elif(random == 2):
            if(arg.upper() == "SCHERE"):
                send("Du hast verloren! Ich hatte Stein.")
            elif(arg.upper() == "STEIN"):
                send("Unentschieden! Ich hatten auch Stein.")
            elif(arg.upper() == "PAPIER"):
                send("Du hast gewonnen! Ich hatte Stein.")
        elif(random == 3):
            if(arg.upper() == "SCHERE"):
                send("Du hast gewonnen! Ich hatte Papier.")
            elif(arg.upper() == "STEIN"):
                send("Du hast verloren! Ich hatte Papier.")
            elif(arg.upper() == "PAPIER"):
                send("Unentschieden! Ich hatten auch Papier.")
    else:
        return send("Bitte schreibe Schere, Stein oder Papier nach /ssp")

def next():
    now = datetime.now()

    time = now.strftime("%H:%M")
    dayNum = datetime.today().weekday()
    weekDays = ["montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag"]
    day = weekDays[dayNum]

    if(dayNum == 5 or dayNum == 6):
        send("Heute ist frei (:")
    else:
        tableToday = timetable[day]
        for i in tableToday:
            if(time < i):
                send("Nächste Stunde haben wir " + tableToday[i])
                break

def bot(msg):
    response = requests.get("https://some-random-api.ml/chatbot/?message=" + msg)
    response = response.json()
    send(response["response"])

time.sleep(10)
login()
time.sleep(10)
enterChat()
time.sleep(10)
global oldMessage
oldMessage = ""
while True:
    gong()
    read()
    if oldMessage != message:
        print("Neue Nachricht: " + message)
        if message.startswith('/calc '):
            calc(message.replace("/calc ", ""))
        elif message == "/corona":
            corona()
            send("Infizierte: " + response[0] + "\nTote: " + response[1] + "\nWiederhergestellte: " + response[2])
        elif(message.startswith('/trans')):
            trans(message.replace("/trans ", ""))
        elif(message == "/help"):
            send("Aktuelle Befehle:\n/help\n   Zeigt alle Befehle an\n/next\n   Zeigt an, was man in der nächsten Stunde hat.\n/calc <Aufgabe>\n   Taschenrechner Plus: + ,  Minus: - ,  Mal: * ,  Geteiltdurch: /\n/trans <Zielsprache> <Text>\n   Übersetzt deinen Text in Deutsch, Englisch oder Französisch.\n   Nach Deutsch: de\n   Nach Englsich: en\n   Nach Französisch: fr\n/ssp <Schere/Stein/Papier>\n   Spiele Schere, Stein oder Papier.")
        elif(message.startswith("/ssp")):
            ssp(message.replace("/ssp ", ""))
        elif(message == "/next"):
            next()
        #else:
            #bot(message)

    oldMessage = message
    time.sleep(1)
