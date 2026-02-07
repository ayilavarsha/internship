import speech_recognition as sr
import pyttsx3
import requests
import json
import datetime
import time
import threading
from schedule import every, run_pending  


engine = pyttsx3.init()
engine.setProperty('rate', 150)  


WEATHER_API_KEY = 'your_openweather_api_key_here'  
NEWS_API_KEY = 'your_newsapi_key_here'  

reminders = []

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen for voice input."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return None

def get_weather(city):
    """Fetch weather information."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"The weather in {city} is {description} with a temperature of {temp} degrees Celsius."
        else:
            return "City not found."
    except:
        return "Unable to fetch weather data."

def get_news():
    """Fetch top news headlines."""
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'ok':
            articles = data['articles'][:5]  
            news = "Here are the top news headlines: "
            for i, article in enumerate(articles, 1):
                news += f"{i}. {article['title']}. "
            return news
        else:
            return "Unable to fetch news."
    except:
        return "Unable to fetch news."

def set_reminder(message, delay_minutes):
    """Set a reminder."""
    def remind():
        time.sleep(delay_minutes * 60)
        speak(f"Reminder: {message}")
    
    threading.Thread(target=remind).start()
    reminders.append(f"Reminder set for {delay_minutes} minutes: {message}")
    return f"Reminder set for {delay_minutes} minutes."

def check_reminders():
    """Background task to check for scheduled reminders (if using schedule library)."""
    while True:
        run_pending()
        time.sleep(1)

def main():
    speak("Hello! I am your voice-activated personal assistant. How can I help you?")
    
    
    threading.Thread(target=check_reminders, daemon=True).start()
    
    while True:
        command = listen()
        if command is None:
            continue
        
        if 'weather' in command:
            speak("Which city?")
            city = listen()
            if city:
                weather_info = get_weather(city)
                speak(weather_info)
        
        elif 'news' in command:
            news_info = get_news()
            speak(news_info)
        
        elif 'reminder' in command or 'remind' in command:
            speak("What should I remind you about?")
            message = listen()
            if message:
                speak("In how many minutes?")
                try:
                    delay = int(listen())
                    response = set_reminder(message, delay)
                    speak(response)
                except:
                    speak("Sorry, I didn't understand the time.")
        
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        
        else:
            speak("I can help with weather, news, or setting reminders. Please try again.")

if __name__ == "__main__":
    main()