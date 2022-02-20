from ast import Return
import email
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def current_city():
    ip_address = find_my_ip()
    city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
    return city

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def send_email(receiver_address:str, subject:str, message:str):
    """[summary]

    Args:
        receiver_address (str): The to email address
        subject (str): Subject of the email message
        message (str): Contents of the email message

    Returns:
        Bool: Successfully sent True or False
    """
    EMAIL = config("EMAIL")
    PASSWORD = config("PASSWORD")
    try:
        # Construct Email
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        # Send Email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.send_message(email)
        return True
                    
    except Exception as e:
        print(e)
        return False

def get_latest_news():
    """[summary]

    Returns:
        [type]: [description]
    """
    NEWS_API_KEY = config("NEWS_API_KEY")
    ENDPOINT = 'https://newsapi.org/v2/top-headlines'
    header = {
            'X-Api-Key': NEWS_API_KEY
        }
    # Query
    params = {
        'country': 'au',
        'category': 'general'
    }
    try:
        response = requests.get(ENDPOINT, params=params, headers=header)
        response.raise_for_status()
        all_articles = response.json()['articles']
        headlines = [article['title'] for article in all_articles]
        return headlines[:5] # Top 5 headlines
    except Exception as e:
        print(e)
        return ['No Articles Returned']

def get_weather_report(city:str):
    APP_ID = config("OPENWEATHER_APP_ID")
    ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather'

    paramaters = {
        'appid': APP_ID,
        'q': city,
        'units' :'metric'
    }
    try:
        response = requests.get(ENDPOINT, params=paramaters)
        response.raise_for_status()
        data = response.json()
        weather = data["weather"][0]["main"]
        temperature = int(data["main"]["temp"])
        feels_like = int(data["main"]["feels_like"])
        low = int(data["main"]["temp_min"])
        high = int(data["main"]["temp_max"])
        current_weather = f'The weather today will be {weather}, with a low of {low} and a high of {high}℃. Currently it is {temperature} and feels like {feels_like}℃'
        return current_weather
    except Exception as e:
        print(e)
        return 'I could not get weather'

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    try:
        response = requests.get("https://icanhazdadjoke.com/", headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["joke"]
    except Exception as e:
        print(e)
        return 'I could not get a joke.'

def get_random_advice():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        response.raise_for_status()
        data = response.json()
        return data['slip']['advice']
    except Exception as e:
        print(e)
        return "I'm sorry i could not give you any advice at this time."