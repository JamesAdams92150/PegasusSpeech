import speech_recognition as sr
import asyncio
import datetime
import random
import websockets
from datetime import datetime
import json


async def time(websocket, path):
    while True:	
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Parler")
            audio = r.listen(source)
            now = datetime.now()
            dateTime = now.strftime("%d/%m/%Y à %H:%M:%S")
        try:
            data = r.recognize_google(audio, language='fr-FR')
            print("A " + dateTime + " vous avez dit: " + data)
            if(data == "red background"):
                await websocket.send(json.dumps({'type': 'commande', 'typeC': 'background', 'color': 'red'}))
            else:
                await websocket.send(json.dumps({'type': 'text', 'dateTime': "Le " + dateTime + " : ", 'text': data}))
                #await websocket.send("Le " + dateTime + " : " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()