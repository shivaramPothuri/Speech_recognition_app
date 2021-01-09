import speech_recognition as sr
import playsound
from gtts import gTTS
import random
import webbrowser
from datetime import datetime
import time
from time import ctime
import os

#simple class for setting name of user

class person:
    name = ''

    def setName(self, name):
        self.name = name

def there_exits(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if(ask):
            speak(ask)
        audio = r.listen(source)   #Listen the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  #audio to text conversition
        except sr.UnknownValueError:
            speak("I didn't get that")
        except sr.RequestError:
            speak("Sorry, the service is down")
        return voice_data

def speak(audio_string):
    tts = gTTS(text = audio_string, lang = 'en', tld="com") # get the string of text as audio_string and speak that text (speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'  #stroing file as audio1133.mp3
    tts.save(audio_file)   # save as mp3
    playsound.playsound(audio_file)
    print(f"siri:{audio_string}")  #print what the app said
    os.remove(audio_file) #remove audio file


def response(voice_data):

     if there_exits(['hey', 'hi', 'hello', 'siri']):  #there_exits(terms)
        greetings  = [f"hey, How Can I Help You {person_obj.name}", f"hello {person_obj.name} how do you do?", f"hey, what's up {person_obj.name}", f"This siri here for you {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings)-1)]
        speak(greet)

     if there_exits(["what is your name", "what's you name", "tell me your name", "name"]):
         if person_obj.name:
             speak("my name is siri")
         else:
             speak("my name is siri.what is you name?")


     if there_exits(['my name is']):
         person_name = voice_data.split("is")[-1].strip() # split the data in voice_data and stores the name of you
         speak(f"Nice to meet you {person_name}, I remember you name")
         person_obj.setName(person_name)  # stroing person_name in class

     if there_exits(["how are you", "how are you doing"]):
         speak(f"Iam doing good, thank you for asking you are so kind of you {person_obj.name}")
         speak(f"What about you {person_name.name}")

     if there_exits(["iam fine ", "iam good", "good, thanks", "fine thanks"]):
         speak(f"that's good ,how can i help you {person_obj.name}")

     if there_exits(["what's the time", "tell me the time", " what time is it"]):
         today = datetime.now()
         d2 = today.strftime("%B %d, %Y %H:%M")
         print(d2)

     if there_exits(["search for", "search"]) and 'youtube' not in voice_data:
         search_item = voice_data.split("for")[-1]
         url = f"https://google.com/search?q={search_item}"
         webbrowser.get().open(url)
         speak(f"Here is what i found for you {search_item} on google")

     if there_exits(["youtube"]):
         search_term = voice_data.spit("for")[-1]
         url = f"https://www.youtube.com/results?search_query={search_term}"
         speak(f"Here is what i found for you {search_item} on google {person_obj.name}")

     if there_exits(['exit', 'quit', 'goodbye', 'bye', 'close']):
         speak("going offline")
         exit()
         

time.sleep(1)
person_obj = person()

while(1):
    voice_data = record_audio()
    response(voice_data)

