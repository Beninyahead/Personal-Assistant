from pprint import pprint

import functions.speech_engine as speech_engine 
import functions.online_operations as online_funcs 
import functions.os_operations as os_funcs 

PRINT_TO_SCREEN_MESSAGE = "For your convenience, I am printing it on the screen sir."

if __name__ == '__main__':
    speech_engine.greet_user()
    while True:
        query = speech_engine.take_user_input().lower()

        if 'open notepad' in query:
            os_funcs.open_notepad()

        elif 'open command prompt' in query or 'open cmd' in query:
            os_funcs.open_cmd()

        elif 'open camera' in query:
            os_funcs.open_camera()

        elif 'open calculator' in query:
            os_funcs.open_calculator()

        elif 'ip address' in query:
            ip_address = online_funcs.find_my_ip()
            speech_engine.speak(f'Your IP Address is {ip_address}.\n {PRINT_TO_SCREEN_MESSAGE}.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speech_engine.speak('What do you want to search on Wikipedia, sir?')
            search_query = speech_engine.take_user_input().lower()
            results = online_funcs.search_on_wikipedia(search_query)
            speech_engine.speak(f"According to Wikipedia, {results}")
            speech_engine.speak(PRINT_TO_SCREEN_MESSAGE)
            print(results)

        elif 'youtube' in query:
            speech_engine.speak('What do you want to play on Youtube, sir?')
            video = speech_engine.take_user_input().lower()
            online_funcs.play_on_youtube(video)

        elif 'search on google' in query:
            speech_engine.speak('What do you want to search on Google, sir?')
            query = speech_engine.take_user_input().lower()
            online_funcs.search_on_google(query)

        elif "send an email" in query:
            speech_engine.speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speech_engine.speak("What should be the subject sir?")
            subject = speech_engine.take_user_input().capitalize()
            speech_engine.speak("What is the message sir?")
            message = speech_engine.take_user_input().capitalize()
            if online_funcs.send_email(receiver_address, subject, message):
                speech_engine.speak("I've sent the email sir.")
            else:
                speech_engine.speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speech_engine.speak("Hope you like this one sir")
            joke = online_funcs.get_random_joke()
            speech_engine.speak(joke)
            speech_engine.speak(PRINT_TO_SCREEN_MESSAGE)
            pprint(joke)

        elif "advice" in query:
            speech_engine.speak("Here's an advice for you, sir")
            advice = online_funcs.get_random_advice()
            speech_engine.speak(advice)
            speech_engine.speak(PRINT_TO_SCREEN_MESSAGE)
            pprint(advice)
        
        elif 'news' in query:
            speech_engine.speak("I'm reading out the latest news headlines, sir")
            speech_engine.speak(online_funcs.get_latest_news())
            speech_engine.speak(PRINT_TO_SCREEN_MESSAGE)
            print(*online_funcs.get_latest_news(), sep='\n')

        elif 'weather' in query:
            speech_engine.speak('What city should i get the weather for?')
            sub_query = speech_engine.take_user_input()
            city = sub_query.lower().split()[0]
            if 'none' in sub_query:
                city = online_funcs.current_city()
            speech_engine.speak(f"Getting weather report for your city {city}")
            speech_engine.speak(online_funcs.get_weather_report(city))

        else:
            speech_engine.speak('Sorry, I could not understand. Could you please say that again?')