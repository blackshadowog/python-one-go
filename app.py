import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import glob
import threading
from datetime import datetime
from urllib.parse import quote_plus
import musiclibrary
import yt_dlp

# pip install pocketsphinx

recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.phrase_threshold = 0.2
recognizer.non_speaking_duration = 0.3
engine = pyttsx3.init() 
newsapi = "<Your Key Here>"
search_target = "google"
last_search_query = ""

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    print("Prime:", text)
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


def play_song(url):
    song_file = None
    try:
        options = {
            "format": "bestaudio/best",
            "outtmpl": "song.%(ext)s",
            "noplaylist": True,
            "js_runtimes": {"node": {}},
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": True,
        }
        with yt_dlp.YoutubeDL(options) as downloader:
            downloader.download([url])

        song_file = next(
            (path for path in glob.glob("song.*") if path.lower().endswith(".mp3")),
            None,
        )
        if not song_file:
            raise FileNotFoundError("yt-dlp did not create an MP3 file")

        pygame.mixer.init()
        pygame.mixer.music.load(song_file)
        pygame.mixer.music.play()
        stopped = False
        with sr.Microphone() as source:
            while pygame.mixer.music.get_busy():
                try:
                    audio = recognizer.listen(
                        source, timeout=0.5, phrase_time_limit=3
                    )
                    command = recognizer.recognize_google(
                        audio, language="en-IN"
                    ).lower()
                    if "stop" in command:
                        pygame.mixer.music.stop()
                        stopped = True
                except (sr.WaitTimeoutError, sr.UnknownValueError):
                    pass
                except sr.RequestError:
                    break
                pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()
        if stopped:
            speak("Playback stopped.")
    except Exception as error:
        print("Song playback error:", error)
        speak("I could not play the full song.")
    finally:
        for downloaded_file in glob.glob("song.*"):
            if os.path.exists(downloaded_file):
                os.remove(downloaded_file)


def open_first_search_result(query):
    try:
        options = {
            "quiet": True,
            "extract_flat": True,
            "noplaylist": True,
            "js_runtimes": {"node": {}},
        }
        with yt_dlp.YoutubeDL(options) as downloader:
            results = downloader.extract_info(
                f"ytsearch1:{query}", download=False
            )
        first_result = (results.get("entries") or [None])[0]
        if not first_result:
            speak("I could not find a first result.")
            return
        video_url = first_result.get("webpage_url") or first_result.get("url")
        webbrowser.open(video_url)
    except Exception as error:
        print("Search playback error:", error)
        speak("I could not open the first result.")


def open_first_search_result_in_background(query):
    threading.Thread(
        target=open_first_search_result,
        args=(query,),
        daemon=True,
    ).start()

def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named prime skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    global last_search_query, search_target
    command = c.lower()
    if command in {"hello", "hi", "hey prime"}:
        speak("Hello. How can I help you?")
    elif "your name" in command or "who are you" in command:
        speak("I am Prime, your voice assistant.")
    elif "time" in command:
        speak(datetime.now().strftime("It is %I:%M %p."))
    elif "date" in command or "today" in command:
        speak(datetime.now().strftime("Today is %A, %B %d, %Y."))
    elif command.startswith("search youtube for "):
        query = c[len("search youtube for "):].strip()
        if query:
            last_search_query = query
            search_target = "youtube"
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={quote_plus(query)}"
            )
        else:
            speak("What should I search for on YouTube?")
    elif command.startswith("search for ") or command.startswith("search "):
        if command.startswith("search for "):
            query = c[len("search for "):].strip()
        else:
            query = c[len("search "):].strip()
        if query:
            if search_target == "youtube":
                last_search_query = query
            if search_target == "youtube":
                webbrowser.open(
                    "https://www.youtube.com/results?search_query="
                    f"{quote_plus(query)}"
                )
            else:
                webbrowser.open(
                    f"https://www.google.com/search?q={quote_plus(query)}"
                )
        else:
            speak("What should I search for?")
    elif command.startswith("open "):
        websites = {
            "google": "https://google.com",
            "facebook": "https://facebook.com",
            "youtube": "https://youtube.com",
            "whatsapp": "https://web.whatsapp.com",
            "linkedin": "https://linkedin.com",
            "github": "https://github.com",
            "instagram": "https://instagram.com",
            "gmail": "https://mail.google.com",
            "chatgpt": "https://chatgpt.com",
            "spotify": "https://open.spotify.com",
        }
        site = command.removeprefix("open ").strip()
        if site in websites:
            webbrowser.open(websites[site])
            search_target = "youtube" if site == "youtube" else "google"
        else:
            speak("I do not know that website yet.")
    elif command.startswith("play first"):
        if last_search_query:
            open_first_search_result_in_background(last_search_query)
        else:
            speak("Search something on YouTube first.")
    elif command.startswith("play"):
        song = " ".join(command.split()[1:])
        link = next((url for name, url in musiclibrary.music.items()
                     if name.lower() == song), None)
        if link:
            play_song(link)
        else:
            speak("I could not find that song.")
    elif "news" in command:
        response = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
        )
        if response.status_code == 200:
            for article in response.json().get("articles", []):
                speak(article["title"])
    else:
        speak(aiProcess(c))


def listen_for_command():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=15, phrase_time_limit=25)
        except sr.WaitTimeoutError:
            return ""

    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        print("You:", command)
        return command
    except sr.UnknownValueError:
        speak("I did not understand that.")
    except sr.RequestError:
        speak("Speech recognition is unavailable right now.")
    return ""


if __name__ == "__main__":
    with sr.Microphone() as source:
        print("Calibrating microphone... Please stay quiet for one second.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
    speak("Prime is ready. Tell me what to do.")
    while True:
        command = listen_for_command().strip()
        if command.lower() in {"exit", "quit"}:
            speak("Prime closed.")
            break
        if command:
            processCommand(command)