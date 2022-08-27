import datetime, colorama, pyttsx3
foreground = colorama.Fore
tts = pyttsx3.init()


def time():
    string = "The time is " + datetime.datetime.today().strftime("%X")
    print(foreground.LIGHTMAGENTA_EX + string)
    tts.say(string)
    tts.runAndWait()


def date():
    string = "The date today is " + str(datetime.date.today())
    print(foreground.LIGHTMAGENTA_EX + string)
    tts.say(string)
    tts.runAndWait()


def whoareyou():
    string = "I am an artificial assistant developed to do mundane tasks. Because my code is modular, I can perform a variety of functions, just add a new module!"
    print(foreground.LIGHTMAGENTA_EX + string)
    tts.say(string)
    tts.runAndWait()
