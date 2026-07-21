import pyjokes  
import pyttsx3

engine = pyttsx3.init()

j = pyjokes.get_joke()
print(j)
engine.say(j)
engine.runAndWait()