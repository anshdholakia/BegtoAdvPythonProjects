def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)



if __name__ =='__main__':
    import requests
    import json
    r=input("Your API key:\n")
    url=('https://newsapi.org/v2/top-headlines?'
         'sources=the-times-of-india&'
         f'apiKey={r}')  #37e7ef8f2fab4666b65eca438c7684a4

    a=requests.get(url)
    text=a.text
    my_json=json.loads(text)
    for i in range(0,11):
        speak(my_json['articles'][i]['title'])
        speak("Next news! Concentrate")